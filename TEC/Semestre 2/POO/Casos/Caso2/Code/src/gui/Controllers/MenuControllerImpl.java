package gui.Controllers;

import java.util.ArrayList;
import java.util.List;

import javax.sound.midi.SysexMessage;

import simulation.Simulation;
import data.DataStorage;
import gui.UI.NearbyStop;
import gui.UI.SimulationConfigurator;

import model.*;

public class MenuControllerImpl implements MenuController{

    private Simulation simulation;
    private DataStorage data;

    public MenuControllerImpl(Simulation simulation) {
        this.simulation = simulation;
        this.data = new DataStorage();
    }

    // Iniciar simulacion
    @Override
    public void handleStart() {
        StopController controller = new StopControllerImpl(simulation);
        NearbyStop nearbyStop = new NearbyStop(controller);
        simulation.setRunning(true);
        simulation.execute();
    }

    @Override
    public void handleLoad() {

        DataStorage dataStorage = new DataStorage();

        simulation.setBusLines(dataStorage.load("Data.dat"));

    }

    @Override
    public void handleSave() {
        
        DataStorage dataStorage = new DataStorage();

        dataStorage.save(simulation.getBusLines(), "Data.dat");

    }

    @Override
    public void handleConfig() {
        
        SCController controller = new SCControllerImpl(simulation);

        SimulationConfigurator simulationConfigurator = new SimulationConfigurator(controller);
        
    }
    
}
