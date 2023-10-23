package gui.UI;

import javax.imageio.ImageIO;
import javax.swing.*;

import gui.Controllers.StopControllerImpl;
import gui.Controllers.UserWindowController;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;

public class UserWindow extends JFrame{
    private JFrame frame;
    private JComboBox<String> lineComboBox;
    private JButton selectLineButton;
    private JLabel actualHourLabel;
    private JLabel paradaActual;
    private JLabel nextBusLabel;
    private JLabel fareLabel;
    private JLabel timeLeftLabel;
    private JButton changeStopButton;
    private JButton exit;
    private Timer HourTimer, BusTimer;

    // ------------------ BusPosition ------------------ //

    class BusAnimation extends JPanel {

        private int busPos = 0; // Posición X del bus
        private int maxPos = 333; // Ancho máximo del panel
        private BufferedImage busImage;
        private BufferedImage stopImageR;
        private BufferedImage stopImageG;
        private String color = "red";

        {
            try {
                busImage = ImageIO.read(new File("src\\gui\\UI\\bus.png"));
                stopImageR = ImageIO.read(new File("src\\gui\\UI\\stopr.png"));
                stopImageG = ImageIO.read(new File("src\\gui\\UI\\stopg.png"));

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        public BusAnimation() {
          
        }
      
        public void updateBus(double percent) {
        
          busPos = (int)(percent * maxPos);
          if (busPos > maxPos) {
            color = "green";
          }
          repaint();
          
        }
      
        @Override
        public void paintComponent(Graphics g) {
      
            super.paintComponent(g);
          
            // Dibujar línea horizontal negra en la parte inferior
            g.setColor(Color.GRAY);
            g.fillRect(0, getHeight()-10, getWidth(), 10);
          
            // Dibujar el bus
            if (color == "green") {
              g.drawImage(stopImageG, maxPos+11, 15, null);
            } else {
              g.drawImage(stopImageR, maxPos+11, 15, null);
            }
            g.drawImage(busImage, busPos, 20, null);
          
          
        }
      
    }

    public UserWindow(UserWindowController userWindowController) {

        int simulationTime = userWindowController.getSimulationTime();

        // Crear la ventana principal
        frame = new JFrame("Ventana de Usuario");
        frame.setResizable(false);
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Crear el panel principal con el color de fondo
        JPanel mainPanel = new JPanel();
        mainPanel.setBackground(Color.decode("#bdffa1"));
        mainPanel.setLayout(new BorderLayout());
        frame.add(mainPanel);

        // Crear el panel superior para la selección de línea y el botón de selección
        JPanel topPanel = new JPanel(new FlowLayout());
        JComboBox<String> stopComboBox = new JComboBox<>(userWindowController.getAllRoutes());
        stopComboBox.setPreferredSize(new Dimension(200, 30));
        stopComboBox.setBackground(Color.decode("#ff887d"));
        topPanel.add(stopComboBox);
        topPanel.add(Box.createRigidArea(new Dimension(10, 0)));
        selectLineButton = new JButton("Seleccionar");
        selectLineButton.setBackground(Color.decode("#ff6b6b"));
        topPanel.add(selectLineButton);
        topPanel.setBorder(BorderFactory.createEmptyBorder(15, 0, 0, 0)); // Agregar espacio de 15px arriba
        mainPanel.add(topPanel, BorderLayout.NORTH);

        // Crear el panel central para la información del bus
        JPanel centerPanel = new JPanel(new GridLayout(0, 1));
        centerPanel.setBorder(BorderFactory.createEmptyBorder(0, 50, 0, 50)); // Agregar margen de 50px a los lados izquierdo y derecho
        actualHourLabel = new JLabel("Hora actual: " + userWindowController.getActualHour());
        centerPanel.add(actualHourLabel);
        paradaActual = new JLabel("Parada seleccionada:" + userWindowController.getActualStop());
        centerPanel.add(paradaActual);
        nextBusLabel = new JLabel("Proximo bus:");
        centerPanel.add(nextBusLabel);
        fareLabel = new JLabel("Tarifa:");
        centerPanel.add(fareLabel);
        timeLeftLabel = new JLabel("Tiempo restante:");
        centerPanel.add(timeLeftLabel);
        BusAnimation busAnimation = new BusAnimation();
        busAnimation.setBackground(Color.decode("#6e8696"));
        busAnimation.setPreferredSize(new Dimension(400, 100));
        centerPanel.add(busAnimation);
        mainPanel.add(centerPanel, BorderLayout.CENTER);


        // Crear el panel inferior para los botones adicionales
        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        changeStopButton = new JButton("Cambiar de Parada");
        changeStopButton.setBackground(Color.decode("#ff0d0d"));
        exit = new JButton("Salir");
        exit.setBackground(Color.decode("#ff6b6b"));
        changeStopButton.setPreferredSize(new Dimension(170, 30));
        exit.setPreferredSize(new Dimension(170, 30));
        bottomPanel.add(changeStopButton);
        bottomPanel.add(exit);
        bottomPanel.setBorder(BorderFactory.createEmptyBorder(15, 0, 15, 0)); // Agregar espacio de 15px abajo
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        // Hacer que los paneles interiores sean transparentes
        topPanel.setOpaque(false);
        bottomPanel.setOpaque(false);
        centerPanel.setOpaque(false);

        // Hacer visible la ventana
        frame.setVisible(true);


        // ------------------ Timers ------------------ //

        // Crear un timer para actualizar la hora actual cada segundo

        HourTimer = new Timer(1000/simulationTime, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                actualHourLabel.setText("Hora actual: " + userWindowController.getActualHour());
            }
        });

        // Crear un timer para actualizar la información del bus cada 10 segundos

        BusTimer = new Timer(0, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selectedLine = (String) stopComboBox.getSelectedItem();
                
                String[] busInfo = userWindowController.selectRoute(selectedLine);

                // Actualizar la etiqueta de información del bus con los datos de la línea seleccionada

                nextBusLabel.setText("Proximo bus: " + busInfo[0]);
                fareLabel.setText("Tarifa: " + busInfo[1]);
                timeLeftLabel.setText("Tiempo restante: " + busInfo[2] + " minutos aprox.");
                
                busAnimation.updateBus(Double.parseDouble(busInfo[3]));

                // Imprimir en consola el porcentaje de la ruta que ha recorrido el bus
            }
        });

        // ------------------ Agregar manejadores de eventos ------------------ //
        
        // Action listener para volver a la ventana de selección de parada

        changeStopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                // Abrir la ventana de seguimiento del bus
                userWindowController.handleChangeStop();
                

                // Cerrar la ventana actual
                frame.setVisible(false);
                frame.dispose();
                
            }
        });

        // Agregar ActionListener al botón de selección de línea
        selectLineButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                BusTimer.setRepeats(true);
                BusTimer.setCoalesce(true);
                BusTimer.setDelay(5000/simulationTime);
                BusTimer.start();
            }
        });

        // Agregar ActionListener al botón de salir

        exit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                userWindowController.handleExit();
                
                frame.setVisible(false);
                frame.dispose();
            }
        });

        HourTimer.start();

        
    }

}
