package Painters;

import Paints.*;
import java.awt.Graphics;

public abstract class Painter {
    protected ShapeStrategy lastShape;

    // Método abstracto que cada pintor implementará para decidir qué dibujar
    public abstract void paint(Graphics g);

    // Método para actualizar la última forma dibujada
    public void setLastShape(ShapeStrategy lastShape) {
        this.lastShape = lastShape;
    }
}
