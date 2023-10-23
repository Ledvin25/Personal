package gui.Controllers;

import gui.UI.NearbyStop;
import model.Stop;

public interface StopController {
    
    public String[] getStopList();

    public void getSelectedStop(String stopName);

    public void setNearbyStop(NearbyStop nearbyStop);
    
}
