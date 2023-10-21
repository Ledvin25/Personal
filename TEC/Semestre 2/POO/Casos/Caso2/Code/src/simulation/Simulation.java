package simulation;

import model.Bus;
import model.BusLine;
//import model.Route;
//import model.Stop;

import java.util.ArrayList;
import java.util.List;
import java.time.LocalTime;


public class Simulation extends Thread {

    // --------------------------------------------- Attributes ---------------------------------------------

    private int simulationTime;
    private List<BusLine> busLines;

    // --------------------------------------------- Getters ---------------------------------------------

    public List<BusLine> getBusLines() {
        return busLines;
    }

    public int getSimulationTime() {
        return simulationTime;
    }

    // --------------------------------------------- Setters ---------------------------------------------

    public void setBusLines(List<BusLine> busLines) {
        this.busLines = busLines;
    }

    public void setSimulationTime(int simulationTime) {
        this.simulationTime = simulationTime;
    }

    // --------------------------------------------- Methods ---------------------------------------------

    // Constructor sin parametros

    public Simulation() {

        this.busLines = new ArrayList<>();

    }

    // Agregar una busLine

    public void addBusLine(BusLine busLine) {
        busLines.add(busLine);
    }

    // Eliminar una busLine

    public void removeBusLine(BusLine busLine) {
        busLines.remove(busLine);
    }

    // Iniciar la simulacion

    public void startSimulation(int x) {
        // Set the start time to 4am
        LocalTime startTime = LocalTime.of(5, 59, 50);

        

        // Set scale time for every bus

        for (BusLine busLine : busLines) {
            busLine.setEscala_tiempo(x);

            for (Bus bus : busLine.getBuses()) {
                bus.setEscala_tiempo(x);
            }
        }
    
        // Loop through each hour of the simulation
        while(startTime.isBefore(LocalTime.of(23, 0, 0))) {
            // Wait for x seconds (1 second = 1 second in simulation time)

            // Print the real time
            System.out.println("Start time: " + startTime);

            try {
                Thread.sleep(1000/x);
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
    }

    // Detener la simulacion

    public void stopSimulation() {
        System.exit(0);
    }

    
    
}
