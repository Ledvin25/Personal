package gui.Controllers;

import java.util.ArrayList;
import java.util.List;

import simulation.Simulation;
import data.DataStorage;
import gui.UI.NearbyStop;
import gui.UI.SimulationConfigurator;
import data.Data;

import model.*;

public class MenuControllerImpl implements MenuController{

    private Simulation simulation;
    private Data data;

    public MenuControllerImpl(Simulation simulation) {
        this.simulation = simulation;
        this.data = new Data();
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

        dataStorage.load();
    }

    @Override
    public void handleSave() {
        List<Bus> buses = new ArrayList<>();
        List<Route> routes = new ArrayList<>();
        List<Stop> stops = new ArrayList<>();
        
        for(BusLine busLine: simulation.getBusLines()) {
            
            for(Bus bus: busLine.getBuses()) {
                buses.add(bus);
            }

            for(Route route: busLine.getRoutes()) {
                routes.add(route);

                for(Stop stop: route.getStops()) {
                    stops.add(stop);
                }
            }

        }

        // Guardar datos

        Data data = new Data(buses, simulation.getBusLines(), routes, stops);
        
        DataStorage dataStorage = new DataStorage();

        dataStorage.save(data);


    }

    @Override
    public void handleConfig() {
        
        SCController controller = new SCControllerImpl(simulation);

        SimulationConfigurator simulationConfigurator = new SimulationConfigurator(controller);
        
    }
    
}
