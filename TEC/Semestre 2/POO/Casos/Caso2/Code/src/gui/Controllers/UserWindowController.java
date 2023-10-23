package gui.Controllers;

public interface UserWindowController {

    public String getActualStop();
    
    public String[] getAllRoutes();

    public void handleChangeStop();

    public String[] selectRoute(String routeName);

    public String getActualHour();

    public int getSimulationTime();

    public void handleExit();
    
}
