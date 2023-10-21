package gui;

import java.util.ArrayList;
import java.util.List;

import model.BusLine;
import model.Route;
import model.Stop;
import simulation.Simulation;

public class StopControllerImpl implements StopController {

    private NearbyStop nearbyStop;
    private Simulation simulation;
    private List<String> stops = new ArrayList<>();

    public StopControllerImpl(Simulation simulation) {
        this.simulation = simulation;
    }

    public void setNearbyStop(NearbyStop nearbyStop) {
        this.nearbyStop = nearbyStop;
    }

    @Override
    public String[] getStopList() {
        
        // Buscar todas las paradas

            // Obtener todas las paradas de todas las lineas de buses

            List<BusLine> busLines = simulation.getBusLines();

            for (BusLine busLine : busLines) {

                List<Route> routes = busLine.getRoutes();

                for (Route route : routes) {

                    List<Stop> stops = route.getStops();

                    for (Stop stop : stops) {

                        // Si la parada no esta en la lista de paradas, agregarla

                        if (!this.stops.contains(stop.getName()))
                        {
                            this.stops.add(stop.getName());
                        }

                    }

                }

            }

            // Convertir la lista de paradas a un arreglo de Strings

            String[] stops = new String[this.stops.size()];
            stops = this.stops.toArray(stops);

            return stops; // Devolver el arreglo de Strings
    }
    
}
