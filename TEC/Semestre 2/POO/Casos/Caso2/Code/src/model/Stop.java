package model;

public class Stop 
{
    private String name;
    private double position; // Distancia a la siguiente parada en la ruta en metros
    private boolean terminal; // Indica si la parada es terminal o no

    public Stop(String name, double position, boolean terminal) {
        this.name = name;
        this.position = position;
        this.terminal = terminal;
    }

    // Constructor sin parametros

    public Stop() {
        this.terminal = false;
    }

    // -------------------------------------  Setters  ------------------------------------- //

    public void setName(String name) {
        this.name = name;
    }

    public void setPosition(double position) {
        this.position = position;
    }

    public void setTerminal(boolean terminal) {
        this.terminal = terminal;
    }

    // -------------------------------------  Getters  ------------------------------------- //

    public String getName() {
        return name;
    }

    public double getPosition() {
        return position;
    }

    public boolean isTerminal() {
        return terminal;
    }
    
}
