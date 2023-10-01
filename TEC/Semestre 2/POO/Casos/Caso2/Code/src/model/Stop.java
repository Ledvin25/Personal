package model;

public class Stop 
{
    private String name;
    private double distance; // Distancia a la siguiente parada en la ruta en metros
    private boolean terminal; // Indica si la parada es terminal o no

    public Stop(String name, double distance, boolean terminal) {
        this.name = name;
        this.distance = distance;
    }

    public String getName() {
        return name;
    }

    public double getDistance() {
        return distance;
    }

    // Método para comprobar si la parada es terminal o no
    public boolean isTerminal() {
        return terminal;
    }
    
}
