package gui.UI;

import javax.swing.*;

import gui.Controllers.StopControllerImpl;
import gui.Controllers.UserWindowController;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserWindow extends JFrame{
    private JFrame frame;
    private JComboBox<String> lineComboBox;
    private JButton selectLineButton;
    private JLabel nextBusLabel;
    private JLabel fareLabel;
    private JLabel timeLeftLabel;
    private JButton changeStopButton;
    private JButton busTrackingButton;

    public UserWindow(UserWindowController userWindowController) {
        // Crear la ventana principal
        frame = new JFrame("Ventana de Usuario");
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
        nextBusLabel = new JLabel("Proximo bus:");
        centerPanel.add(nextBusLabel);
        fareLabel = new JLabel("Tarifa:");
        centerPanel.add(fareLabel);
        timeLeftLabel = new JLabel("Tiempo restante:");
        centerPanel.add(timeLeftLabel);
        changeStopButton = new JButton("Cambiar de Parada");
        changeStopButton.setBackground(Color.decode("#ff0d0d"));
        centerPanel.add(changeStopButton);
        busTrackingButton = new JButton("Seguimiento del Bus");
        busTrackingButton.setBackground(Color.decode("#ff6b6b"));
        centerPanel.add(busTrackingButton);
        mainPanel.add(centerPanel, BorderLayout.CENTER);

        // Crear el panel inferior para los botones adicionales
        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        changeStopButton.setPreferredSize(new Dimension(170, 30));
        busTrackingButton.setPreferredSize(new Dimension(170, 30));
        bottomPanel.add(changeStopButton);
        bottomPanel.add(busTrackingButton);
        bottomPanel.setBorder(BorderFactory.createEmptyBorder(15, 0, 15, 0)); // Agregar espacio de 15px abajo
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        // Hacer que los paneles interiores sean transparentes
        topPanel.setOpaque(false);
        bottomPanel.setOpaque(false);
        centerPanel.setOpaque(false);

        // Hacer visible la ventana
        frame.setVisible(true);

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

        // Action listener para abrir la ventana de seguimiento del bus

        busTrackingButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                // Abrir la ventana de seguimiento del bus
                userWindowController.handleShowBusPosition();

                // Cerrar la ventana actual
                frame.setVisible(false);
                frame.dispose();

            }
        });

        
        // Agregar ActionListener al botón de selección de línea
        selectLineButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Implementar la lógica para obtener y mostrar la información de la línea seleccionada
                String selectedLine = (String) stopComboBox.getSelectedItem();
                
                String[] busInfo = userWindowController.selectRoute(selectedLine);

                // Actualizar la etiqueta de información del bus con los datos de la línea seleccionada

                nextBusLabel.setText("Proximo bus: " + busInfo[0]);
                fareLabel.setText("Tarifa: " + busInfo[1]);
                timeLeftLabel.setText("Tiempo restante: " + busInfo[2] + " minutos aprox.");
                
            }
        });
    }
}
