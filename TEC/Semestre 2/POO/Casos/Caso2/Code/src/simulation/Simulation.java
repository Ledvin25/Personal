package simulation;

import javax.swing.SwingWorker;

import model.*;
import java.util.ArrayList;
import java.util.List;
import java.time.LocalTime;
import data.JSONLoader;


public class Simulation extends SwingWorker<Void, Void> {

    // --------------------------------------------- Attributes ---------------------------------------------

    private int simulationTime;
    private List<BusLine> busLines;
    private LocalTime startTime = LocalTime.of(5, 0, 0);
    private boolean running = false;

    // --------------------------------------------- Getters ---------------------------------------------

    public List<BusLine> getBusLines() {
        return busLines;
    }

    public int getSimulationTime() {
        return simulationTime;
    }

    public LocalTime getStartTime() {
        return startTime;
    }

    // --------------------------------------------- Setters ---------------------------------------------

    public void setBusLines(List<BusLine> busLines) {
        this.busLines = busLines;
    }

    public void setSimulationTime(int simulationTime) {
        this.simulationTime = simulationTime;
    }

    public void setStartTime(LocalTime startTime) {
        this.startTime = startTime;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    // --------------------------------------------- Methods ---------------------------------------------

    // Constructor sin parametros

    public Simulation(int simulationTime) {

        this.busLines = new ArrayList<>();
        this.simulationTime = simulationTime;
    }

    // Agregar una busLine

    public void addBusLine(BusLine busLine) {
        busLines.add(busLine);
    }

    // Eliminar una busLine

    public void removeBusLine(BusLine busLine) {
        busLines.remove(busLine);
    }

    // Cargar datos del JSON

    public void loadData() {
        JSONLoader jsonLoader = new JSONLoader();
        
        // Crear objetos

        // Crear lista de busLine
        for(String enterprise : jsonLoader.getEnterprise()) 
        {
            // Obtener hora y minuto de inicio
            int horaInicio = Integer.parseInt(jsonLoader.getHoraInicio(enterprise).substring(0, 2));
            int minutosInicio = Integer.parseInt(jsonLoader.getHoraInicio(enterprise).substring(3,4));

            // Obtener hora y minuto de fin

            int horaFin = Integer.parseInt(jsonLoader.getHoraFin(enterprise).substring(0,2));
            int minutosFin = Integer.parseInt(jsonLoader.getHoraFin(enterprise).substring(3, 4));

            // Crear busLine y agregar

            BusLine busLine = new BusLine(LocalTime.of(horaInicio, minutosInicio), LocalTime.of(horaFin, minutosFin), enterprise);
            busLines.add(busLine);

            // Crear buses

            for(String bus: jsonLoader.getBuses(enterprise))
            {
                String[] infoBus = bus.split(":");
                String license = infoBus[0];
                int capacity = Integer.parseInt(infoBus[1]);

                Bus busObject = new Bus(license, capacity);
                busLine.addBus(busObject);
            }

            // Crear rutas

            for(String ruta : jsonLoader.getRutas(enterprise))
            {
                String[] infoRuta = ruta.split(":");

                String nameRoute = infoRuta[0];
                float fare = Float.parseFloat(infoRuta[1]);
                int id = Integer.parseInt(infoRuta[2]);

                Route route = new Route(id, fare, nameRoute);
                busLine.addRoute(route);

                // Crear paradas

                for(String parada: jsonLoader.getParadas(enterprise, nameRoute))
                {
                    String[] infoParada = parada.split(":");

                    String nameStop = infoParada[0];
                    double position = Integer.parseInt(infoParada[1]);
                    boolean terminal = Boolean.parseBoolean(infoParada[2]);

                    Stop stop = new Stop(nameStop, position, terminal);
                    route.addStop(stop);
                }
            }
        }
        
    }

    // Iniciar la simulacion
    @Override
    protected Void doInBackground() throws Exception {

        if (simulationTime <= 0) {
            System.out.println("El tiempo de simulacion debe ser mayor a 0");
            return null;
        }
        // Set scale time for every bus

        for (BusLine busLine : busLines) {
            busLine.setEscala_tiempo(simulationTime);

            for (Bus bus : busLine.getBuses()) {
                bus.setEscala_tiempo(simulationTime);
            }
        }
    
        // Loop through each hour of the simulation
        while(running && startTime.isBefore(LocalTime.of(23, 0, 0))) {
            // Wait for simulationTime seconds (1 second = 1 second in simulation time)

            // Print the real time
            System.out.println("Start time: " + startTime);

            try {
                Thread.sleep(1000/simulationTime);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
    
            // Increment the start time by 1 hour
            startTime = startTime.plusSeconds(1);
    
            // Start every bus line
            for (BusLine busLine : busLines) {
                busLine.start(startTime);
            }
        }

        return null;
    }

    // Detener la simulacion

    public void stopSimulation() {
        // Detener cada busLine
        for (BusLine busLine : busLines) {
            for (Bus bus : busLine.getBuses()) {
                bus.endTrip();
            }
        }
        running = false;
        cancel(true);
    }

    
    
}
