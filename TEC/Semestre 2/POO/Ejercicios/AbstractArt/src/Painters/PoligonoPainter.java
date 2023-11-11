package Painters;

import java.awt.Color;
import java.awt.Graphics;
import java.util.List;
import java.util.ArrayList;

public class PoligonoPainter implements PainterStrategy{
    
  private int[] xPoints;
  private int[] yPoints;
  private int numPoints;
  private Color color;

  public PoligonoPainter(int[] xPoints, int[] yPoints, Color color) {
    this.xPoints = xPoints;
    this.yPoints = yPoints;
    this.numPoints = xPoints.length;
    this.color = color;
  }

  public Color getColor() {
    return color;
  }

  public List<Integer> getShapeInfo() {
    List<Integer> shapeInfo = new ArrayList<Integer>();
    for (int i = 0; i < numPoints; i++) {
      shapeInfo.add(xPoints[i]);
      shapeInfo.add(yPoints[i]);
    }
    return shapeInfo;
  }

  public void draw(Graphics g) {
    // Establecer color
    g.setColor(color);  

    // Rellena el polígono
    g.fillPolygon(xPoints, yPoints, numPoints);
  }

}
