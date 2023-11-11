package Paints;

import java.util.List;

import javax.swing.JPanel;

import Painters.PainterStrategy;

import java.util.ArrayList;
import java.awt.Graphics;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AbstractPainting extends JPanel{

    private int totalPaints;
    
    private List<PainterStrategy> painters;

    public AbstractPainting(int totalPaints) {
        this.painters = new ArrayList<PainterStrategy>();
        this.totalPaints = totalPaints;
    }

    //---------------------------------------------//

    public Iterator getIterator() {
        return new AbstractPaintingIterator(painters); 
      }

    public void addShape(PainterStrategy shape) {
        this.painters.add(shape);
    }

    public void paintComponent(Graphics g)
    {
        for(int i = 0; i < totalPaints*painters.size(); i++){
            for (PainterStrategy painter : painters) {

                painter.draw(g);
                painter.setLastShape(painter);
                painter.notifyObservers();
            }
        }
        System.out.println("Finzalido");
    }
}
