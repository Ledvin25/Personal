package Paints;

import java.util.List;

import javax.swing.JPanel;

import Painters.PainterStrategy;

import java.util.ArrayList;
import java.awt.Graphics;

public class AbstractPainting extends JPanel{
    
    private List<PainterStrategy> shapes;

    public AbstractPainting() {
        this.shapes = new ArrayList<PainterStrategy>();
    }

    //---------------------------------------------//

    public Iterator getIterator() {
        return new AbstractPaintingIterator(shapes); 
      }

    public void addShape(PainterStrategy shape) {
        this.shapes.add(shape);
    }

    public void paintComponent(Graphics g)
    {
        for (PainterStrategy shape : shapes) {

            shape.draw(g);
        }
    }
}
