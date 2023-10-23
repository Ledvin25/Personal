package model;

import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonIgnore;

import java.time.LocalTime;

public class BusLine extends Thread{
    
    @JsonIgnore
    private LocalTime startTime;
    @JsonIgnore
    private LocalTime endTime;

    private String name;

    private List<Bus> buses;
    private List<Route> routes;
    private int escala_tiempo;

    // Constructor

    public BusLine(LocalTime startTime, LocalTime endTime, String name) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.buses = new ArrayList<>();
        this.routes = new ArrayList<>();
        this.name = name;
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
    
    public void setEscala_tiempo(int escala_tiempo) {
        this.escala_tiempo = escala_tiempo;
    }

    public void setEnterprise(String name) {
        this.name = name;
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

    public int getEscala_tiempo() {
        return escala_tiempo;
    }

    public String getEnterprise() {
        return name;
    }

    // -------------------------------------  Methods  ------------------------------------- //

    // changeBusRoute
    public void changeBusRoute(String licensePlate, int route_id) {
        for(Bus bus : buses) {
            if(bus.getLicensePlate() == licensePlate) {
                for(Route route : routes) {
                    if(route.getRoute() == route_id) {
                        bus.setCurrentRoute(route);
                        return;
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

    // -------------------------------------  Threads  ------------------------------------- //

    public void start(LocalTime CurrentTime)
    {
        if(CurrentTime.isAfter(startTime) && CurrentTime.isBefore(endTime))
        {
            // Iniciar los buses disponibles
            for(Bus bus : buses)
            {
                if(bus.getPosition() == 0 && bus.isRunning() == false)
                {
                    // Asignar ruta de forma aleatoria
                    int random = (int) (Math.random() * routes.size());
                    bus.setCurrentRoute(routes.get(random));

                    // Iniciar viaje
                    bus.startTrip();
                }
            }

            // Devolver los buses que ya llegaron a la terminal

            for(Bus bus : buses)
            {
                if(bus.getPosition() != 0 && bus.isRunning() == false && bus.getCurrentRoute().getStops().get(bus.getStop_index()).isTerminal() == true)
                {
                    bus.run();
                }
            }
        }
    }
}
