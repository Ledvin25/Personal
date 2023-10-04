package model;

import java.util.ArrayList;
import java.util.List;

public class Route {

    private List<Stop> stops;
    private int route_id;

    public Route(int route_id) {
        this.stops = new ArrayList<>();
        this.route_id = route_id;
    }

    public void addStop(Stop stop) {
        stops.add(stop);
    }

    public void removeStop(Stop stop) {
        stops.remove(stop);
    }

    public List<Stop> getStops() {
        return stops;
    }

    public List<String> getStopsName() {

        List<String> stopsName = new ArrayList<>();

        for(int index = 0; index < stops.size(); index++)
        {
            stopsName.add(stops.get(index).getName());
        }

        return stopsName;
    }

    public int getRoute() {
        return route_id;
    }

    // Método para calcular la distancia total de la ruta
    public double calculateTotalDistance() {

        double distance = 0.0d;

        for (int i = 0; i < stops.size() - 1; i++) {

            distance += stops.get(i).getPosition();

        }
        return distance;
    }

}