package Paints;

import java.awt.Color;
import java.awt.Graphics;

public class Lunar implements ShapeStrategy{
    
    private int x;
    private int y; 
    private int radius;
    private Color color;
  
    public Lunar(int x, int y, int radius, Color color) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.color = color;
    }

    public void draw(Graphics g) {
        // Establecer color
        g.setColor(color);
    
        // Dibujar círculo 
        g.fillOval(x, y, radius, radius);
    
    }

}
