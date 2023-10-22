package gui.Controllers;

import gui.UI.NearbyStop;
import model.Stop;

public interface StopController {
    
    public String[] getStopList();

    // Get the selected stop

    public void getSelectedStop(String stopName);

    public void setNearbyStop(NearbyStop nearbyStop);
    
}
