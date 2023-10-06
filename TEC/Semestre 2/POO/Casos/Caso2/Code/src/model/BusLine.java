package model;

import java.util.ArrayList;
import java.util.List;
import java.time.LocalTime;

public class BusLine {
    
    private LocalTime startTime;
    private LocalTime endTime;
    private List<Bus> buses;
    private List<Route> routes;

    // Constructor

    public BusLine(LocalTime startTime, LocalTime endTime) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.buses = new ArrayList<>();
        this.routes = new ArrayList<>();
    }

    // Constructor sin parametros

    public BusLine() {
        this.buses = new ArrayList<>();
        this.routes = new ArrayList<>();
    }

    // -------------------------------------  Setters  ------------------------------------- //

    public void setStartTime(LocalTime startTime) {
        this.startTime = startTime;
    }

    public void setEndTime(LocalTime endTime) {
        this.endTime = endTime;
    }

    public void setBuses(List<Bus> buses) {
        this.buses = buses;
    }

    public void setRoutes(List<Route> routes) {
        this.routes = routes;
    }
    

    // -------------------------------------  Getters  ------------------------------------- //

    public LocalTime getStartTime() {
        return startTime;
    }

    public LocalTime getEndTime() {
        return endTime;
    }

    public List<Bus> getBuses() {
        return buses;
    }

    public List<Route> getRoutes() {
        return routes;
    }

    // -------------------------------------  Methods  ------------------------------------- //

    // changeBusRoute
    public void changeBusRoute(int licensePlate, int route_id) {
        for(Bus bus : buses) {
            if(bus.getLicensePlate() == licensePlate) {
                for(Route route : routes) {
                    if(route.getRoute() == route_id) {
                        bus.setCurrentRoute(route);
                    }
                }
            }
        }
    }

    //addRoute
    public void addRoute(Route route) {
        routes.add(route);
    }

    //removeRoute
    public void removeRoute(Route route) {
        routes.remove(route);
    }

    //addBus
    public void addBus(Bus bus) {
        buses.add(bus);
    }

    //removeBus
    public void removeBus(Bus bus) {
        buses.remove(bus);
    }
}
