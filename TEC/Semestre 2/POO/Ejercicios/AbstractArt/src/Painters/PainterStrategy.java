package Painters;

import java.awt.Graphics;
import java.util.List;
import java.awt.Color;

public interface PainterStrategy {
    
    public void draw(Graphics g);

    public List<Integer> getShapeInfo();

    public Color getColor();
}
