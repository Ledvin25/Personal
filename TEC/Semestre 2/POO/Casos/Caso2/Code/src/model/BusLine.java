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

    // Set and get startTime

    public LocalTime getStartTime() {
        return startTime;
    }

    public void setStartTime(LocalTime startTime) {
        this.startTime = startTime;
    }

    // Set and get endTime

    public LocalTime getEndTime() {
        return endTime;
    }

    public void setEndTime(LocalTime endTime) {
        this.endTime = endTime;
    }

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
