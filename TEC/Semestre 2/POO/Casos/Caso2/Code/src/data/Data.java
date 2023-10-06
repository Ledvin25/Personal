package data;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import model.Bus;
import model.BusLine;
import model.Route;
import model.Stop;
import java.util.List;

@JsonAutoDetect(fieldVisibility = JsonAutoDetect.Visibility.ANY)
public class Data {
    private List<Bus> buses;
    private List<BusLine> busLines;
    private List<Route> routes;
    private List<Stop> stops;

    public Data() {
        // Constructor sin argumentos requerido por Jackson
    }

    public Data(List<Bus> buses, List<BusLine> busLines, List<Route> routes, List<Stop> stops) {
        this.buses = buses;
        this.busLines = busLines;
        this.routes = routes;
        this.stops = stops;
    }

    public List<Bus> getBuses() {
        return buses;
    }

    public void setBuses(List<Bus> buses) {
        this.buses = buses;
    }

    public List<BusLine> getBusLines() {
        return busLines;
    }

    public void setBusLines(List<BusLine> busLines) {
        this.busLines = busLines;
    }

    public List<Route> getRoutes() {
        return routes;
    }

    public void setRoutes(List<Route> routes) {
        this.routes = routes;
    }

    public List<Stop> getStops() {
        return stops;
    }

    public void setStops(List<Stop> stops) {
        this.stops = stops;
    }
}