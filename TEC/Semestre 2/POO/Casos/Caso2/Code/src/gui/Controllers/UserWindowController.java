package gui.Controllers;

import model.Stop;
import simulation.Simulation;

public interface UserWindowController {
    
    public String[] getAllRoutes();

    public void handleChangeStop();

    public void handleShowBusPosition();

    public String[] selectRoute(String routeName);
    
}
