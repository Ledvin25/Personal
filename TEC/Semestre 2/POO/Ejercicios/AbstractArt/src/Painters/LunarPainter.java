package Painters;

import java.awt.Color;
import java.awt.Graphics;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;


public class LunarPainter extends PainterStrategy{

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

    @Override
    public int[] getShapeInfo() {
      int[] pos = {x, y};

      return pos;
    }

    public Color getColor() {
      return color;
    }

    public void draw(Graphics g) {

      int[] lastShapeInfo = lastShape.getShapeInfo();

      if(lastShape != null)
      {
        if (lastShape instanceof PoligonoPainter) {
            // Si es un polígono, pinta en cualquier lugar que no sea donde está el polígono
            x = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y = getRandomDifferentCoordinate(lastShapeInfo[1]);
            color = getRandomColor();
        } else if (lastShape instanceof LunarPainter) {
            // Si es un lunar, pinta en cualquier lugar que no sea donde estaba el lunar
            x = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y = getRandomDifferentCoordinate(lastShapeInfo[1]);
            color = getRandomColor();
        } else if (lastShape instanceof LineaPainter) {
            // Si es una línea, pinta en otra zona donde no estaba esa línea
            x = getRandomDifferentCoordinate(lastShapeInfo[0]);
            y = getRandomDifferentCoordinate(lastShapeInfo[1]);
            color = getRandomColor();
        }
      }
      // Establecer color
      g.setColor(color);

      // Dibujar círculo
      g.fillOval(x, y, radius, radius);
    
    }

    public void update(PainterStrategy lastShape) {
        this.lastShape = lastShape;
    }

    private Color getRandomColor() {
        Random random = new Random();
        return new Color(random.nextInt(256), random.nextInt(256), random.nextInt(256));
    }

    // Método para obtener una coordenada diferente random
    private int getRandomDifferentCoordinate(int coordinate) {
        Random random = new Random();
        int newCoordinate = random.nextInt(400); // Ajusta el rango según el tamaño de tu lienzo
        while (newCoordinate == coordinate) {
            newCoordinate = random.nextInt(400); // Ajusta el rango según el tamaño de tu lienzo
        }
        return newCoordinate;
    }

}
