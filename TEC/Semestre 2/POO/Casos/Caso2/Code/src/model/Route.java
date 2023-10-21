package model;

import java.util.ArrayList;
import java.util.List;

public class Route {

    private List<Stop> stops;
    private int route_id;
    private float fare;

    public Route(int route_id, float fare) {
        this.stops = new ArrayList<>();
        this.route_id = route_id;
        this.fare = fare;
    }

    // Constructor sin parametros

    // -------------------------------------  Setters  ------------------------------------- //

    public void setStops(List<Stop> stops) {
        this.stops = stops;
    }

    public void setRoute(int route_id) {
        this.route_id = route_id;
    }

    public void setFare(float fare) {
        this.fare = fare;
    }

    // -------------------------------------  Getters  ------------------------------------- //

    public List<Stop> getStops() {
        return stops;
    }

    public int getRoute() {
        return route_id;
    }

    public float getFare() {
        return fare;
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

        double distance = stops.get(stops.size() - 1).getPosition();

        return distance;
    }

}