package gui;

import java.util.ArrayList;
import java.util.List;

import model.BusLine;
import model.Route;
import model.Stop;
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

    

    
}
