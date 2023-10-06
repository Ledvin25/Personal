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


    // --------------------------------------------- Constructor ---------------------------------------------

    public App(Stop stop) 
    {
        this.stop = stop;
    }

    // --------------------------------------------- Methods ---------------------------------------------

    public String[] findNearbyBuses(BusLine busLine)
    {

        // Lista para guardar las rutas que pasan por la parada
        List<Route> routes = new ArrayList<Route>();

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

        // Lista para guardar los buses que pasan por la parada
        List<Bus> buses = new ArrayList<Bus>();

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

        // Lista para guardar las placas de los buses que pasan por la parada
        List<String> licensePlates = new ArrayList<String>();
        
        for(Bus bus : buses)
        {
            licensePlates.add(Integer.toString(bus.getLicensePlate()));
        }

        // Retornar la lista de placas de los buses que pasan por la parada
        return licensePlates.toArray(new String[0]);
    }

    // Obtener el proximo bus
    public String getNextBus()
    {
        return null;
    }

    // Obtener el bus anterior
    public String getPrevBus()
    {
        return null;
    }

    // Obtener el tiempo de espera
    public String getBusInfo(Bus bus)
    {
        return null;
    }

    // Obtener el tiempo restante
    public String getTimeRemaining(Bus bus)
    {
        return null;
    }
}
