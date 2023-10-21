package gui;

import model.Stop;

public interface StopController {
    
    public String[] getStopList();

    // Get the selected stop

    public String getSelectedStop(String stopName);
    
}
