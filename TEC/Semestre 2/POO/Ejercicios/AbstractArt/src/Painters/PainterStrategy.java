package Painters;

import java.awt.Graphics;
import java.util.List;
import java.util.ArrayList;

public abstract class PainterStrategy implements Observer{
    
    protected PainterStrategy lastShape;
    private List<Observer> observers;

    public PainterStrategy() {
        this.observers = new ArrayList<Observer>();
    }

    public void setLastShape(PainterStrategy lastShape) {
        this.lastShape = lastShape;
        notifyObservers();
    }

    public abstract void draw(Graphics g);

    public abstract int[] getShapeInfo();

    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(lastShape);
        }
    }

}
