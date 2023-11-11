package Factory;

import Painters.*;
import java.awt.Color;
import java.util.Random;

public class LineaPainterFactory implements PainterFactory{
    private static final Random random = new Random();

    public PainterStrategy createPainter() {
        // Genera valores aleatorios para inicializar el LineaPainter
        int x1 = random.nextInt(500);  // Ajusta según el rango deseado
        int x2 = random.nextInt(500);
        int y1 = random.nextInt(500);
        int y2 = random.nextInt(500);
        int stroke = random.nextInt(5) + 1;  // Ajusta según el rango deseado
        Color color = generateRandomColor();

        // Crea e inicializa el LineaPainter con valores aleatorios
        return new LineaPainter(x1, x2, y1, y2, stroke, color);
    }

    // Método para generar un color aleatorio
    private Color generateRandomColor() {
        int red = random.nextInt(256);
        int green = random.nextInt(256);
        int blue = random.nextInt(256);
        return new Color(red, green, blue);
    }
}
