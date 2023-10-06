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

    // Constructor sin parametros

    // -------------------------------------  Setters  ------------------------------------- //

    public void setStops(List<Stop> stops) {
        this.stops = stops;
    }

    public void setRoute(int route_id) {
        this.route_id = route_id;
    }

    // -------------------------------------  Getters  ------------------------------------- //

    public List<Stop> getStops() {
        return stops;
    }

    public int getRoute() {
        return route_id;
    }

    // -------------------------------------  Otros  ------------------------------------- //

    // Método para agregar paradas a la ruta

    public void addStop(Stop stop) {
        stops.add(stop);
    }

    // Método para eliminar paradas de la ruta

    public void removeStop(Stop stop) {
        stops.remove(stop);
    }

    // Método para obtener el nombre de las paradas de la ruta

    public List<String> getStopsName() {

        List<String> stopsName = new ArrayList<>();

        for(int index = 0; index < stops.size(); index++)
        {
            stopsName.add(stops.get(index).getName());
        }

        return stopsName;
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