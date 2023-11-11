package Painters;

import Paints.*;
import java.awt.Graphics;

class LunarPainter extends Painter {
    @Override
    public void paint(Graphics g) {
        if (lastShape instanceof Lunar) {
            // Obtener el radio del último círculo dibujado
            int lastRadius = ((Lunar) lastShape).getRadius();

            // Definir el número de círculos concéntricos a dibujar
            int numCircles = 5;

            // Dibujar círculos concéntricos
            for (int i = 1; i <= numCircles; i++) {
                int currentRadius = lastRadius + i * 20; // Ajusta el factor multiplicativo según tus necesidades
                g.drawOval(lastShape.getX(), lastShape.getY(), currentRadius, currentRadius);
            }
        } else {
            // Si la última forma no es un círculo, dibuja un círculo por defecto
            g.drawOval(50, 50, 30, 30);
        }
    }
}