package Factory;

import java.awt.Color;
import java.util.Random;

import Painters.*;


public class PoligonoPainterFactory implements PainterFactory {
    private static final Random random = new Random();

    @Override
    public PainterStrategy createPainter(int red, int blue, int green, int priority) {
        // Genera valores aleatorios para inicializar el PoligonoPainter
        int numPoints = random.nextInt(5) + 3;  // Ajusta según el rango deseado (mínimo 3 puntos)
        int[] xPoints = generateRandomPoints(500, numPoints);
        int[] yPoints = generateRandomPoints(500, numPoints);
        Color color = generateRandomColor();

        // Crea e inicializa el PoligonoPainter con valores aleatorios
        return new PoligonoPainter(xPoints, yPoints, color);
    }

    // Método para generar puntos aleatorios dentro de un rango especificado
    private int[] generateRandomPoints(int range, int numPoints) {
        int[] points = new int[numPoints];
        for (int i = 0; i < numPoints; i++) {
            points[i] = random.nextInt(range);
        }
        return points;
    }

    // Método para generar un color aleatorio
    private Color generateRandomColor() {
        int red = random.nextInt(256);
        int green = random.nextInt(256);
        int blue = random.nextInt(256);
        return new Color(red, green, blue);
    }
}

