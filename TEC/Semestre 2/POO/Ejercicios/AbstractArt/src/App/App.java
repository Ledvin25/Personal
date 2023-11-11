package App;

import Paints.*;
import java.awt.*;

import javax.swing.JFrame;

import Painters.LineaPainter;
import Painters.LunarPainter;
import Painters.PoligonoPainter;

public class App {
    public static void main(String[] args) {
        
        // Test con una linea y un circulo usando el patron Iterator

        // Crear un objeto de tipo AbstractPainting

        AbstractPainting abstractPainting = new AbstractPainting();

        // Crear un objeto de tipo Line

        LineaPainter line = new LineaPainter(0, 0, 100, 100, 3, Color.RED);

        // Crear un objeto de tipo Lunar

        LunarPainter lunar = new LunarPainter(100, 100, 100, Color.BLUE);

        // Crear un objeto de tipo Polygon

        int[] xPoints = { 100, 200, 300 };
        int[] yPoints = { 100, 200, 100 };
        PoligonoPainter polygon = new PoligonoPainter(xPoints, yPoints, Color.GREEN);

        // Agregar los objetos a la lista de shapes del objeto de tipo AbstractPainting

        abstractPainting.addShape(line);

        abstractPainting.addShape(lunar);

        abstractPainting.addShape(polygon);

        // Crear un objeto de tipo JFrame

        JFrame frame = new JFrame();

        // Agregar el objeto de tipo AbstractPainting al JFrame

        frame.add(abstractPainting);

        // Establecer el tamaño del JFrame

        frame.setSize(500, 500);

        // Establecer la operacion por defecto al cerrar el JFrame

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Establecer el JFrame como visible

        frame.setVisible(true);
        
        
    }
}
