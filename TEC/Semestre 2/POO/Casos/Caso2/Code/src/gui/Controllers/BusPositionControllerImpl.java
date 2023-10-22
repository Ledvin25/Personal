package gui.Controllers;

import gui.UI.BusPosition;
import simulation.Simulation;

public class BusPositionControllerImpl implements BusPositionController {

    private Simulation simulation;
    private BusPosition busPosition;

    public BusPositionControllerImpl(Simulation simulation) {
        this.simulation = simulation;
    }

    @Override
    public void setBusPosition(BusPosition busPosition) {
        this.busPosition = busPosition;
    }

    
}
