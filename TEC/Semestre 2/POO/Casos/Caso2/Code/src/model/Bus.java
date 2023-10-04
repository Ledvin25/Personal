package model;

import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class Bus {

    // Atibutos base
    private int licensePlate; // Placa del bus
    private int capacity; // Capacidad de pasajeros
    private double position; // Posición en la ruta en metros
    private Route currentRoute; // Ruta actual
    private int escala_tiempo = 1; // Escala de tiempo de simulación (por defecto, 1 segundo en el programa = 1 segundo en la vida real)

    // Atributos para el control de velocidad
    private double targetSpeed = 80.0; // Velocidad objetivo en km/h
    private double maxSpeedVariation = 15.0; // Variación máxima de velocidad en km/h
    private double speed = 0.0; // Velocidad inicial
    private int stop_index = 1; // Índice de la parada actual

    // Temporizador para el control de velocidad
    private Timer speedTimer = new Timer();

    // Constructor
    public Bus(int licensePlate, int capacity) {
        this.licensePlate = licensePlate;
        this.capacity = capacity;;
    }

    // Método para obtener la ruta actual
    public Route getCurrentRoute() {
        return currentRoute;
    }

    // Método para establecer la ruta actual
    public void setCurrentRoute(Route currentRoute) {
        this.currentRoute = currentRoute;
    }

    // Método para obtener la placa del bus
    public int getLicensePlate() {
        return licensePlate;
    }

    // Método para establecer la placa del bus
    public void setLicensePlate(int licensePlate) {
        this.licensePlate = licensePlate;
    }

    // Método para obtener la velocidad actual
    public double getSpeed() {
        return speed;
    }

    // Método para obtener la posición actual
    public double getPosition() {
        return position;
    }

    // Método para obtener la capacidad
    public int getCapacity() {
        return capacity;
    }

    // Método para obtener la escala de tiempo
    public int getEscala_tiempo() {
        return escala_tiempo;
    }

    // Método para establecer la escala de tiempo
    public void setEscala_tiempo(int escala_tiempo) {
        this.escala_tiempo = escala_tiempo;
    }

    // Iniciar viaje
    public void startTrip() {
        // Iniciar el temporizador para aumentar la velocidad gradualmente
        speedTimer.scheduleAtFixedRate(new SpeedChangeTask(), 0, 1000 / escala_tiempo); // Cada 1 segundo (en la vida real) dividido por la escala de tiempo
    }

    // Finalizar viaje
    public void endTrip() {
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

    // SpeedChangeTask
    private class SpeedChangeTask extends TimerTask {
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
                            Thread.sleep(3000 / escala_tiempo); // Espera 5 segundos (en la vida real) divididos por la escala de tiempo
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }

                        speedTimer = new Timer(); // Crea un nuevo temporizador para reanudar
                        speedTimer.scheduleAtFixedRate(new SpeedChangeTask(), 0, 1000 / escala_tiempo); // Cada 1 segundo (en la vida real) dividido por la escala de tiempo
                        
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
