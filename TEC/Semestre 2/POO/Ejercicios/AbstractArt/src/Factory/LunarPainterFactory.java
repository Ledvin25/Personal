package Factory;

import java.awt.Color;
import java.util.Random;

import Painters.*;

public class LunarPainterFactory implements PainterFactory {
    private static final Random random = new Random();

    @Override
    public PainterStrategy createPainter() {
        // Genera valores aleatorios para inicializar el LunarPainter
        int x = random.nextInt(500);  // Ajusta según el rango deseado
        int y = random.nextInt(500);
        int radius = random.nextInt(50) + 10;  // Ajusta según el rango deseado
        Color color = generateRandomColor();

        // Crea e inicializa el LunarPainter con valores aleatorios
        return new LunarPainter(x, y, radius, color);
    }

    // Método para generar un color aleatorio
    private Color generateRandomColor() {
        int red = random.nextInt(256);
        int green = random.nextInt(256);
        int blue = random.nextInt(256);
        return new Color(red, green, blue);
    }
}

