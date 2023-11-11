package Paints;

import java.util.List;

import javax.swing.JPanel;

import java.util.ArrayList;
import java.awt.Graphics;

public class AbstractPainting extends JPanel{
    
    private List<ShapeStrategy> shapes;

    public AbstractPainting() {
        this.shapes = new ArrayList<ShapeStrategy>();
    }

    //---------------------------------------------//

    public Iterator getIterator() {
        return new AbstractPaintingIterator(shapes); 
      }

    public void addShape(ShapeStrategy shape) {
        this.shapes.add(shape);
    }

    public void paintComponent(Graphics g)
    {
        for (ShapeStrategy shape : shapes) {

            shape.draw(g);
        }
    }
}
