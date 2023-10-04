package model;
import java.time.LocalTime;

public class testBusLine {
    
    // main

    public static void main(String[] args) {
        
        BusLine busLine = new BusLine(LocalTime.of(6, 0), LocalTime.of(22, 0));


        // Crear 6 paradas con nombres mas reales y dos terminales

        Stop stop1 = new Stop("Terminal Norte", 0.0d);
        Stop stop2 = new Stop("Parada 1", 300.0d);
        Stop stop3 = new Stop("Parada 2", 700.0d);
        Stop stop4 = new Stop("Terminal Sur", 1000.0d);
        stop4.setTerminal(true);

        // Crear 2 rutas

        Route route1 = new Route(1);
        Route route2 = new Route(2);

        route1.addStop(stop1);
        route1.addStop(stop2);
        route1.addStop(stop3);
        route1.addStop(stop4);

        route2.addStop(stop1);
        route2.addStop(stop4);

        // Agregar rutas a la linea de buses

        busLine.addRoute(route1);
        busLine.addRoute(route2);

        // Crear 3 buses

        Bus bus1 = new Bus(1, 40);
        Bus bus2 = new Bus(2, 40);
        Bus bus3 = new Bus(3, 40);

        // Agregar buses a la linea de buses

        busLine.addBus(bus1);
        busLine.addBus(bus2);
        busLine.addBus(bus3);

        // Asignar rutas a los buses

        busLine.changeBusRoute(1, 1);
        busLine.changeBusRoute(2, 2);
        busLine.changeBusRoute(3, 1);

        // Iniciar viajes de los buses, que el bus y 3 salgan al mismo tiempo y que el 2 salga 10 segundos despues

        // Imprimir las rutas de los buses

        //System.out.println("Bus : " + bus1.getCurrentRoute().getStopsName());

        bus1.startTrip();
        bus2.startTrip();

        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        bus3.startTrip();


    
    }


}
