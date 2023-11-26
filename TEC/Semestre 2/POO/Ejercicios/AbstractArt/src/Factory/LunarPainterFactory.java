package Factory;

import java.awt.Color;
import java.util.Random;

import Painters.*;

public class LunarPainterFactory implements PainterFactory {
    private static final Random random = new Random();

    @Override
    public PainterStrategy createPainter(int red, int blue, int green, int priority) {
        // Genera valores aleatorios para inicializar el LunarPainter
        int x = random.nextInt(500);  // Ajusta según el rango deseado
        int y = random.nextInt(500);
        int radius = random.nextInt(50) + 10;  // Ajusta según el rango deseado
        Color color = generateRandomColor(red, blue, green);

        // Crea e inicializa el LunarPainter con valores aleatorios
        return new LunarPainter(x, y, radius, color);
    }

    // Método para generar un color aleatorio
    private Color generateRandomColor(int baseRed, int baseGreen, int baseBlue) {
        int red = Math.max(0, Math.min(255, baseRed + random.nextInt(101) - 50));
        int green = Math.max(0, Math.min(255, baseGreen + random.nextInt(101) - 50));
        int blue = Math.max(0, Math.min(255, baseBlue + random.nextInt(101) - 50));
        return new Color(red, green, blue);
    }
}

