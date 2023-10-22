package gui.Controllers;

import java.util.ArrayList;
import java.util.List;

import gui.UI.BusPosition;
import gui.UI.NearbyStop;
import gui.UI.UserWindow;
import model.*;
import simulation.Simulation;

public class UserWindowControllerImpl implements UserWindowController {

    private UserWindow userWindow;
    private Simulation simulation;
    private String stopString;

    public UserWindowControllerImpl(Simulation simulation, String stopString) {
        this.simulation = simulation;
        this.stopString = stopString;
    }

    public void setUserWindow(UserWindow userWindow) {
        this.userWindow = userWindow;
    }

    @Override
    public String[] getAllRoutes() {

        // Crear lista de rutas que contengan la parada seleccionada

        List<Route> routes = new ArrayList<>();

        // Obtener todas las lineas de buses

        List<BusLine> busLines = simulation.getBusLines();

        // Buscar las rutas que contengan la parada seleccionada

        for (BusLine busLine : busLines) {

            for (Route route : busLine.getRoutes()) {

                for (Stop stop : route.getStops()) {

                    if (stop.getName().equals(stopString)) {

                        routes.add(route);

                    }

                }

            }

        }

        // Convertir la lista de rutas a un arreglo de Strings

        String[] routesString = new String[routes.size()];

        for (int i = 0; i < routes.size(); i++) {

            routesString[i] = routes.get(i).getName();

        }

        return routesString;
    }

    @Override
    public void handleChangeStop() {

        StopControllerImpl stopController = new StopControllerImpl(simulation);

        // Abrir la ventana de selección de parada
        NearbyStop nearbyStop = new NearbyStop(stopController);

    }

    @Override
    public void handleShowBusPosition() {

        BusPositionControllerImpl busPositionController = new BusPositionControllerImpl(simulation);

        // Abrir la ventana de seguimiento del bus
        BusPosition busPosition = new BusPosition(busPositionController);

    }

    @Override
    public String[] selectRoute(String routeName) {
        // Buscar el bus que se encuentra mas cerca de la parada seleccionada

        // Variables para almacenar la información del bus, la ruta y la parada

        Bus mostCloseBus = null;
        Route mostCloseRoute = null;
        Stop nearbyStop = null;

        // Array para la información del bus

        String[] busInfo = new String[3];
        double mostCloseBusDistance = 0.0d;

        // Obtener todas las lineas de buses

        List<BusLine> busLines = simulation.getBusLines();

        // Buscar las rutas que contengan la parada seleccionada

        for (BusLine busLine : busLines) {

            for (Route route : busLine.getRoutes()) {

                if (route.getName().equals(routeName)) {

                    for (Stop stop : route.getStops()) {

                        if (stop.getName().equals(stopString)) {

                            for (Bus bus : busLine.getBuses()) {

                                if(bus.getCurrentRoute().getName() == routeName)
                                {
                                    if(bus.getTimeToStop(stop) > 0 && (bus.getDistanceToStop(stop) < mostCloseBusDistance || mostCloseBusDistance == 0.0d)) 
                                    {
                                        mostCloseBusDistance = bus.getDistanceToStop(stop);
                                        mostCloseBus = bus;
                                        mostCloseRoute = route;
                                        nearbyStop = stop;
                                    }
                                }

                            }

                        }

                    }

                }

            }

        }


        // Obtener la información del bus

        try {

            if(mostCloseBus == null || mostCloseRoute == null || nearbyStop == null) throw new Exception();

            busInfo[0] = String.valueOf(mostCloseBus.getLicensePlate());
            busInfo[1] = String.valueOf(mostCloseRoute.getFare());

            // Obtener la parte entera del tiempo restante
            int timeLeft = (int) mostCloseBus.getTimeToStop(nearbyStop);
            
            // Agregar el tiempo restante a la información del bus
            busInfo[2] = String.valueOf(timeLeft);

            return busInfo;

        } catch (Exception e) {

            String[] error = {"No hay buses disponibles", "", ""};

            return error;

        }

        
        
        
        
    }
}
