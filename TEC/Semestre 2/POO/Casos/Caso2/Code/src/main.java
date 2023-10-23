import gui.Controllers.MenuController;
import gui.Controllers.MenuControllerImpl;
import gui.UI.Menu;
import simulation.Simulation;

public class main {
    
    public static void main(String[] args) {

        Simulation simulation = new Simulation(1);
        simulation.loadData();

        MenuController controller = new MenuControllerImpl(simulation);

        Menu menu = new Menu(controller);
        
    }
}
