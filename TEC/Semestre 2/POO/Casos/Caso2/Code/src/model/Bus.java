package model;

import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

import com.fasterxml.jackson.annotation.JsonIgnore;

public class Bus extends Thread{

    // Atibutos base
    String licensePlate; // Placa del bus
    private int capacity; // Capacidad de pasajeros
    private double position; // Posición en la ruta en metros
    private Route currentRoute; // Ruta actual
    private boolean isRunning; // Indicador de si el bus está en movimiento
    private int escala_tiempo = 1; // Escala de tiempo de simulación (por defecto, 1 segundo en el programa = 1 segundo en la vida real)

    // Atributos para el control de velocidad
    private double targetSpeed = 80.0; // Velocidad objetivo en km/h
    private double maxSpeedVariation = 15.0; // Variación máxima de velocidad en km/h
    private double speed = 0.0; // Velocidad inicial
    private int stop_index = 1; // Índice de la parada actual

    // Temporizador para el control de velocidad
    @JsonIgnore
    private Timer speedTimer;

    // Constructor
    public Bus(String licensePlate, int capacity) {
        this.licensePlate = licensePlate;
        this.capacity = capacity;
        this.position = 0.0d;
        this.currentRoute = null;
        this.isRunning = false;
    }

    // Constructor sin parametros

    public Bus() {
    }

    // -------------------------------------  Setters  ------------------------------------- // 

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public void setPosition(double position) {
        this.position = position;
    }

    public void setCurrentRoute(Route currentRoute) {
        this.currentRoute = currentRoute;
    }

    public void setEscala_tiempo(int escala_tiempo) {
        this.escala_tiempo = escala_tiempo;
    }

    public void setTargetSpeed(double targetSpeed) {
        this.targetSpeed = targetSpeed;
    }

    public void setMaxSpeedVariation(double maxSpeedVariation) {
        this.maxSpeedVariation = maxSpeedVariation;
    }

    public void setSpeed(double speed) {
        this.speed = speed;
    }

    public void setStop_index(int stop_index) {
        this.stop_index = stop_index;
    }

    public void setSpeedTimer(Timer speedTimer) {
        this.speedTimer = speedTimer;
    }

    // -------------------------------------  Getters  ------------------------------------- //

    public String getLicensePlate() {
        return licensePlate;
    }

    public int getCapacity() {
        return capacity;
    }

    public double getPosition() {
        return position;
    }

    public Route getCurrentRoute() {
        return currentRoute;
    }

    public boolean isRunning() {
        return isRunning;
    }

    public int getEscala_tiempo() {
        return escala_tiempo;
    }

    public double getTargetSpeed() {
        return targetSpeed;
    }

    public double getMaxSpeedVariation() {
        return maxSpeedVariation;
    }

    public double getSpeed() {
        return speed;
    }

    public int getStop_index() {
        return stop_index;
    }

    public Timer getSpeedTimer() {
        return speedTimer;
    }

    // -------------------------------------  Metodos  ------------------------------------- //

    // Iniciar viaje
    public void startTrip() {

        if (currentRoute == null) {
            System.out.println("No se ha asignado una ruta al bus");
            return;
        }

        isRunning = true; // Indicar que el bus está en movimiento

        speedTimer = new Timer();
        
        // Iniciar el temporizador para aumentar la velocidad gradualmente
        speedTimer.scheduleAtFixedRate(new BusMove(), 0, 1000 / escala_tiempo); // Cada 1 segundo (en la vida real) dividido por la escala de tiempo
    }

    // Finalizar viaje
    public void endTrip() {
        isRunning = false; // Indicar que el bus está detenido
        // Cancelar el temporizador al finalizar el viaje
        speedTimer.cancel();
    }

    // Get distance to next stop 

    public double getDistanceToStop(Stop stop) {
        for(int i = 0; i < currentRoute.getStops().size(); i++)
        {
            if(currentRoute.getStops().get(i).getName().equals(stop.getName()))
            {
                return currentRoute.getStops().get(i).getPosition() - position;
            }
        }

        return 0.0d;
    }

    // Get time to next stop in minutes

    public double getTimeToStop(Stop stop) {
        for(int i = 0; i < currentRoute.getStops().size(); i++)
        {
            if(currentRoute.getStops().get(i).getName().equals(stop.getName()))
            {
                // Retornar el tiempo en minutos
                return ((currentRoute.getStops().get(i).getPosition() - position)/(16.667))/60;
            }
        }

        return 0.0d;
    }

    // Devolver el bus a la terminal

    @Override
    public void run()
    {
        double time = currentRoute.calculateTotalDistance()/(22.2222); // Calcular tiempo de viaje de vuelta

        isRunning = true; // Indicar que el bus está en movimiento

        // Esperar a que el bus llegue a la terminal
        try {
            Thread.sleep((long) (time * 1000/escala_tiempo));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Devolver el bus a la terminal
        position = 0;
        stop_index = 1;

        isRunning = false; // Indicar que el bus está detenido
    }

    // BusMove
    private class BusMove extends TimerTask {
        private int elapsedTime = 0; // Tiempo transcurrido en segundos
        private boolean parada = false; // Indicador de pausa

        @Override
        public void run() {

            // Imprimir la velocidad actual (puedes adaptarlo a tus necesidades)
            System.out.println("Bus: " + licensePlate + " Posicion actual: " + position + " metros");

            elapsedTime++;
            Stop next_stop = currentRoute.getStops().get(stop_index);

            // Arrancar
            if (elapsedTime <= 3 && !parada) {
                // Aumentar la velocidad gradualmente hasta llegar a 80 km/h en 3 segundos
                speed = (targetSpeed / 3) * elapsedTime;
            }
            // Hacer Parada
            else if (position <= next_stop.getPosition() + 15 && position >= next_stop.getPosition() - 15) {
                // Desacelerar gradualmente al acercarse a la parada hasta llegar a 0 km/h

                speed = 0.0d;
                System.out.println("Bus: " + licensePlate + " Parada: " + next_stop.getName());

                // Finalizar si es terminal
                if(next_stop.isTerminal())
                {
                    endTrip();
                    System.out.println("Viaje finalizado");
                }
                else
                {
                    // Esperar para que los pasajeros suban o bajen
                    if (!parada) 
                    {
                        parada = true;
                        endTrip();

                        try {
                            Thread.sleep(3000); // Espera 3 segundos (en la vida real) divididos por la escala de tiempo
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }

                        speedTimer = new Timer(); // Crea un nuevo temporizador para reanudar
                        speedTimer.scheduleAtFixedRate(new BusMove(), 0, 1000 / escala_tiempo); // Cada 1 segundo (en la vida real) dividido por la escala de tiempo
                        
                        // Aumentar el índice de la parada actual
                        stop_index++;
                        //System.out.println("Indice de parada: " + stop_index);

                    }
                }
            } 
            // Simular velocidad por trafico y demas
            else 
            {
                // Generar una variación aleatoria en la velocidad
                Random rand = new Random();
                double randomVariation = (rand.nextDouble() * 2 - 1) * maxSpeedVariation;
                speed = targetSpeed + randomVariation;
            }

            // Actualizar la posición del bus
            position += speed / (3.6 * escala_tiempo); // 1 km/h = 0.277777778 m/s
        }
    }
}
