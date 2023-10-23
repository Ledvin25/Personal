
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;


import data.*;
import model.Bus;
import model.BusLine;
import model.Route;
import model.Stop;
import simulation.Simulation;
import gui.*;
import gui.Controllers.StopController;
import gui.Controllers.StopControllerImpl;
import gui.UI.NearbyStop;
public class firsttest {
    
    // main

    public static void main(String[] args) {
        
        // Lista de busLine

        List<Stop> stops = new ArrayList<>();
        
        BusLine busLine = new BusLine(LocalTime.of(6, 0), LocalTime.of(6, 10), "Lumaca");

        // Agregar busLine a la lista de busLine

        Simulation simulation = new Simulation(5);

        simulation.addBusLine(busLine);

        // Crear 6 paradas con nombres mas reales y dos terminales

        Stop stop1 = new Stop("Terminal Norte", 0.0d);
        Stop stop2 = new Stop("Parada 1", 300.0d);
        Stop stop3 = new Stop("Parada 2", 3000.0d);
        Stop stop4 = new Stop("Terminal Sur", 6000.0d);
        stop4.setTerminal(true);

        stops.add(stop1);
        stops.add(stop2);
        stops.add(stop3);
        stops.add(stop4);

        // Crear 2 rutas

        Route route1 = new Route(1, 620, "Ruta 1");
        Route route2 = new Route(2, 620, "Ruta 2");

        route1.addStop(stop1);
        route1.addStop(stop2);
        route1.addStop(stop3);
        route1.addStop(stop4);

        route2.addStop(stop1);
        route2.addStop(stop4);

        // Agregar rutas a la linea de buses

        busLine.addRoute(route1);
        busLine.addRoute(route2);

        // Crear 3 buses

        Bus bus1 = new Bus(1, 40);
        Bus bus2 = new Bus(2, 40);
        Bus bus3 = new Bus(3, 40);

        // Agregar buses a la linea de buses

        busLine.addBus(bus1);
        busLine.addBus(bus2);
        busLine.addBus(bus3);

        // Iniciar viajes de los buses, que el bus y 3 salgan al mismo tiempo y que el 2 salga 10 segundos despues

        // Imprimir las rutas de los buses

        //System.out.println("Bus : " + bus1.getCurrentRoute().getStopsName());

        // Iniciar la simulacion

        //simulation.startSimulation(10);

        StopController controller = new StopControllerImpl(simulation);

        // Crear la interfaz grafica

        NearbyStop nearbyStop = new NearbyStop(controller);

        // Iniciar simulacion

        simulation.startSimulation();

        


    }


}
