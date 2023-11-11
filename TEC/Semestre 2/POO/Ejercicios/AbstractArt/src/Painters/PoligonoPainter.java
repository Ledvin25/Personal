package Painters;

import java.awt.Color;
import java.awt.Graphics;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class PoligonoPainter extends PainterStrategy{

  private int[] xPoints;
  private int[] yPoints;
  private int numPoints;
  private Color color;

  public PoligonoPainter(int[] xPoints, int[] yPoints, Color color) {
    this.xPoints = xPoints;
    this.yPoints = yPoints;
    this.numPoints = xPoints.length;
    this.color = color;
    lastShape = null;
  }

  public Color getColor() {
    return color;
  }

  @Override
  public int[] getShapeInfo() {
    int[] pos = {xPoints[0], yPoints[0]};

    return pos;
  }

  @Override
  public void draw(Graphics g) {
    int[] lastShapeInfo = lastShape.getShapeInfo();

    if(lastShapeInfo != null){
       if (lastShape instanceof PoligonoPainter) {
            // Si es otro polígono, pinta en otra zona donde no estaba ese polígono
            for (int i = 0; i < numPoints; i++) {
                xPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[0]);
                yPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[1]);
            }
            color = getRandomColor();
        } else if (lastShape instanceof LunarPainter) {
            // Si es un lunar, pinta en otra zona donde no estaba el lunar
            for (int i = 0; i < numPoints; i++) {
                xPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[0]);
                yPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[1]);
            }
            color = getRandomColor();
        } else if (lastShape instanceof LineaPainter) {
            // Si es una línea, pinta en otra zona donde no estaba esa línea
            // Cambia la lógica según tus necesidades
            for (int i = 0; i < numPoints; i++) {
                xPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[0]);
                yPoints[i] = getRandomDifferentCoordinate(lastShapeInfo[1]);
            }
            color = getRandomColor();
        }
      }

        // Establecer color
        g.setColor(color);

        // Rellena el polígono
        g.fillPolygon(xPoints, yPoints, numPoints);
  }

  public void update(PainterStrategy lastShape) {
    this.lastShape = lastShape;
  }

  private Color getRandomColor() {
        Random random = new Random();
        return new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256));
    }

    private int getRandomDifferentCoordinate(int coordinate) {
        Random random = new Random();
        int newCoordinate = random.nextInt(400); // Ajusta el rango según el tamaño de tu lienzo
        while (newCoordinate == coordinate) {
            newCoordinate = random.nextInt(400); // Ajusta el rango según el tamaño de tu lienzo
        }
        return newCoordinate;
    }
}
