package simulation;

import model.Bus;
import model.BusLine;
import model.Route;
import model.Stop;
import java.util.List;
import java.time.LocalTime;


public class Simulation extends Thread {

    // Lista de busLines

    private List<BusLine> busLines;

    // --------------------------------------------- Getters ---------------------------------------------

    public List<BusLine> getBusLines() {
        return busLines;
    }

    // --------------------------------------------- Setters ---------------------------------------------

    // --------------------------------------------- Methods ---------------------------------------------

    // Constructor sin parametros

    public Simulation() {}

    // Agregar una busLine

    public void addBusLine(BusLine busLine) {
        busLines.add(busLine);
    }

    // Eliminar una busLine

    public void removeBusLine(BusLine busLine) {
        busLines.remove(busLine);
    }

    // Iniciar la simulacion

    
    
}
