package App;

import Paints.*;
import java.awt.*;

import javax.swing.JFrame;

import Factory.LineaPainterFactory;
import Factory.LunarPainterFactory;
import Factory.PoligonoPainterFactory;
import Painters.LineaPainter;
import Painters.LunarPainter;
import Painters.PoligonoPainter;
import Painters.PainterStrategy;

public class App {
    public static void main(String[] args) {
        
        // Test

        AbstractPainting painting = new AbstractPainting(100);
        
        // Crear fábricas
        LineaPainterFactory lineaFactory = new LineaPainterFactory();
        LunarPainterFactory lunarFactory = new LunarPainterFactory();
        PoligonoPainterFactory poligonoFactory = new PoligonoPainterFactory();

        // Crear pintores
        PainterStrategy lineaPainter = lineaFactory.createPainter(0,0,255,1);
        PainterStrategy lunarPainter = lunarFactory.createPainter(0,0,255,1);
        PainterStrategy poligonoPainter = poligonoFactory.createPainter(0,0,255,1);

        // Agregar observadores
        lineaPainter.addObserver(lunarPainter);
        lineaPainter.addObserver(poligonoPainter);
        lunarPainter.addObserver(poligonoPainter);
        lunarPainter.addObserver(lineaPainter);
        poligonoPainter.addObserver(lineaPainter);
        poligonoPainter.addObserver(lunarPainter);

        // Agregar pintores a la pintura
        painting.addShape(lineaPainter);
        painting.addShape(lunarPainter);
        painting.addShape(poligonoPainter);

        // Crear ventana


        JFrame frame = new JFrame("Abstract Painting");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setResizable(false);
        frame.setVisible(true);

        
        frame.add(painting);
        
    }
}
