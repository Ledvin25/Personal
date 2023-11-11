package Painters;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.BasicStroke;
import java.awt.Graphics2D;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;

public class LineaPainter extends PainterStrategy{

    private int x1;
    private int x2;
    private int y1;
    private int y2; 
    private int stroke;
    private Color color;
  
    public LineaPainter(int x1, int x2, int y1, int y2, int stroke, Color color) {
      this.x1 = x1;
      this.y2 = x2;
      this.x2 = y1;
      this.y1 = y2;
      this.stroke = stroke;
      this.color = color;
    }

    public Color getColor() {
      return color;
    }

    @Override
    public int[] getShapeInfo() {
      int[] pos = {x1, y1};

      return pos;
    }

    public void draw(Graphics g) {
      if (lastShape != null){
      int[] lastShapeInfo = lastShape.getShapeInfo();

        if (lastShape instanceof PoligonoPainter) {
            // Si es un polígono, pinta en otra zona donde no estaba ese polígono
            x1 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y1 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            x2 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            y2 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            color = getRandomColor();
            stroke = getRandomStroke();
        } else if (lastShape instanceof LunarPainter) {
            // Si es un lunar, pinta en otra zona donde no estaba el lunar
            x1 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y1 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            x2 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            y2 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            color = getRandomColor();
            stroke = getRandomStroke();
        } else if (lastShape instanceof LineaPainter) {
            // Si es otra línea, pinta en otra zona donde no estaba esa línea
            x1 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y1 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            x2 = getRandomDifferentCoordinate(lastShapeInfo[1]);
            y2 = getRandomDifferentCoordinate(lastShapeInfo[0]);
            color = getRandomColor();
            stroke = getRandomStroke();
        }
      }
      // Establecer color
      g.setColor(color);

      // Establecer ancho del trazo
      Graphics2D g2d = (Graphics2D) g;
      g2d.setStroke(new BasicStroke(stroke));

      // Dibujar línea
      g.drawLine(x1, y1, x2, y2);
    
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

    private int getRandomStroke() {
        return new Random().nextInt(10) + 1; // Ajusta el rango según tus necesidades
    }

}
