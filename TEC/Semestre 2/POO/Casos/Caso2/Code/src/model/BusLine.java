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

    // -------------------------------------  Threads  ------------------------------------- //

    void start(LocalTime CurrentTime)
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
                if(bus.getPosition() != 0 && bus.isRunning() == false)
                {
                    double time = bus.getCurrentRoute().calculateTotalDistance()/(22.2222); // Calcular tiempo de viaje de vuelta

                    // Esperar a que el bus llegue a la terminal
                    try {
                        Thread.sleep((long) (time * 1000));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    // Devolver el bus a la terminal
                    bus.setPosition(0);
                    bus.setStop_index(0);
                }
            }
        }
    }
}
