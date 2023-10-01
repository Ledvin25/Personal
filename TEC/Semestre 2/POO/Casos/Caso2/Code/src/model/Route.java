package model;

import java.util.ArrayList;
import java.util.List;

public class Route {

    private List<Stop> stops;

    public Route() {
        this.stops = new ArrayList<>();
    }

    public void addStop(Stop stop) {
        stops.add(stop);
    }

    public void removeStop(Stop stop) {
        stops.remove(stop);
    }

    // Método para calcular la distancia total de la ruta
    public double calculateTotalDistance() {
        double totalDistance = 0.0;
        for (int i = 0; i < stops.size() - 1; i++) {
            totalDistance += stops.get(i).getDistance();
        }
        return totalDistance; // en metros
    }
}
