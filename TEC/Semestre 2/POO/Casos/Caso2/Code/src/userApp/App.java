// Anteriormente StopLogic
package userApp;

import model.Stop;
import model.BusLine;
import model.Route;
import model.Bus;
import simulation.Simulation;
import java.util.ArrayList;
import java.util.List;

public class App {

    // --------------------------------------------- Attributes ---------------------------------------------

    private Stop stop;
    private Simulation simulation;


    // --------------------------------------------- Constructor ---------------------------------------------

    public App(Stop stop, Simulation simulation) 
    {
        this.stop = stop;
        this.simulation = simulation;
    }

    // --------------------------------------------- Methods ---------------------------------------------

    public List<Bus> getBusesByStop()
    {
        // Lista de las lineas que hay en simulation
        List<BusLine> busLines = simulation.getBusLines();

        // Lista para guardar las rutas que pasan por la parada
        List<Route> routes = new ArrayList<Route>();

        for (BusLine busLine : busLines)
        {
            for (Route route : busLine.getRoutes())
            {
                for (Stop stop : route.getStops())
                {
                    if (stop.equals(this.stop))
                    {
                        routes.add(route);
                    }
                }
            }
        }

        // Lista para guardar los buses que pasan por la parada
        List<Bus> buses = new ArrayList<Bus>();

        for (BusLine busLine : busLines)
        {
            for(Bus bus : busLine.getBuses())
            {
                for(Route route : routes)
                {
                    if(bus.getCurrentRoute().equals(route))
                    {
                        buses.add(bus);
                    }
                }
            }
        }

        return buses;
    }

    // Obtener el bus siguiente
    public Bus getNextBus()
    {
        List<Bus> buses = getBusesByStop();

        for(Bus bus : buses)
        {
            if(bus.getDistanceToStop(stop) <= 200)
            {
                return bus;
            }
        }

        return null;
    }

    // Obtener el tiempo de espera
    public String getBusInfo()
    {
        Bus bus = getNextBus();

        // Encontrar la ruta del bus
        Route route = bus.getCurrentRoute();

        // Sacar la tarifa de la ruta
        float fare = route.getFare();

        // Retornar el tiempo la placa y la tarifa

        return "Placa: " + bus.getLicensePlate() + " Tarifa: " + fare;
    }

    // Obtener el tiempo restante
    public String getTimeRemaining(Bus bus)
    {
        // Calcular el tiempo restante para que llegue el bus
        double timeRemaining = bus.getDistanceToStop(stop) / bus.getSpeed();

        // Retornar el tiempo restante
        return "Tiempo restante: " + timeRemaining + " minutos";
    }
}
