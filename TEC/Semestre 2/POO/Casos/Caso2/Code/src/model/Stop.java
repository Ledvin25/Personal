package model;

public class Stop 
{
    private String name;
    private double position; // Distancia a la siguiente parada en la ruta en metros
    private boolean terminal; // Indica si la parada es terminal o no

    public Stop(String name, double position) {
        this.name = name;
        this.position = position;
        this.terminal = false;
    }

    // set terminal
    public void setTerminal(boolean terminal) {
        this.terminal = terminal;
    }

    // getters

    public String getName() {
        return name;
    }

    public double getPosition() {
        return position;
    }

    // Método para comprobar si la parada es terminal o no
    public boolean isTerminal() {
        return terminal;
    }
    
}
