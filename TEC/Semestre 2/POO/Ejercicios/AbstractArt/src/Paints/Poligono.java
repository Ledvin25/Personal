package Paints;

import java.awt.Color;
import java.awt.Graphics;

public class Poligono implements ShapeStrategy{
    
  private int[] xPoints;
  private int[] yPoints;
  private int numPoints;
  private Color color;

  public Poligono(int[] xPoints, int[] yPoints, Color color) {
    this.xPoints = xPoints;
    this.yPoints = yPoints;
    this.numPoints = xPoints.length;
    this.color = color;
  }

  public void draw(Graphics g) {
    // Establecer color
    g.setColor(color);  

    // Rellena el polígono
    g.fillPolygon(xPoints, yPoints, numPoints);
  }

}
