package Paints;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.BasicStroke;
import java.awt.Graphics2D;


public class Linea implements ShapeStrategy{
    
    private int x1;
    private int x2;
    private int y1;
    private int y2; 
    private int stroke;
    private Color color;
  
    public Linea(int x1, int x2, int y1, int y2, int stroke, Color color) {
      this.x1 = x1;
      this.y2 = x2;
      this.x2 = y1;
      this.y1 = y2;
      this.stroke = stroke;
      this.color = color;
    }

    public void draw(Graphics g) {
        // Establecer color
        g.setColor(color);
        
        // Establecer ancho del trazo
        Graphics2D g2d = (Graphics2D) g;
        g2d.setStroke(new BasicStroke(stroke));

        // Dibujar línea
        g.drawLine(x1, y1, x2, y2);
    
    }

}
