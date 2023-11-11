package Painters;

import java.awt.Color;
import java.awt.Graphics;
import java.util.List;
import java.util.ArrayList;

public class LunarPainter implements PainterStrategy{
    
    private int x;
    private int y; 
    private int radius;
    private Color color;
  
    public LunarPainter(int x, int y, int radius, Color color) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.color = color;
    }

    public List<Integer> getShapeInfo() {
      List<Integer> shapeInfo = new ArrayList<Integer>();
      shapeInfo.add(x);
      shapeInfo.add(y);
      shapeInfo.add(radius);
      return shapeInfo;
    }

    public Color getColor() {
      return color;
    }

    public void draw(Graphics g) {
        // Establecer color
        g.setColor(color);
    
        // Dibujar círculo 
        g.fillOval(x, y, radius, radius);
    
    }

}
