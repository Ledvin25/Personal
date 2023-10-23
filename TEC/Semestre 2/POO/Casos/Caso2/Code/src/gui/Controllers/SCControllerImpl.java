package gui.Controllers;

import java.time.LocalTime;

import simulation.Simulation;

public class SCControllerImpl implements SCController{

    private Simulation simulation;

    public SCControllerImpl(Simulation simulation) {
        this.simulation = simulation;
    }

    @Override
    public void handleConfiguration(String simulationTime, String startTime) {
        
        String[] infoTime = startTime.split(":");

        int hour = Integer.parseInt(infoTime[0]);
        int minute = Integer.parseInt(infoTime[1]);

        simulation.setSimulationTime(Integer.parseInt(simulationTime));
        simulation.setStartTime(LocalTime.of(hour, minute));
    }
    
}
