package gui.UI;

import javax.swing.*;

import gui.Controllers.SCController;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimulationConfigurator extends JFrame {
    private JTextField simulationTimeField;
    private JTextField startTimeField;

    public SimulationConfigurator(SCController controller) {
        setTitle("Configuración");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel(new GridLayout(3, 2));

        // Etiqueta para "Simulation Time"
        JLabel simulationTimeLabel = new JLabel("Simulation Time:");
        simulationTimeLabel.setForeground(Color.GRAY);
        panel.add(simulationTimeLabel);

        // Campo de entrada de texto para "Simulation Time"
        simulationTimeField = new JTextField();
        simulationTimeField.setForeground(Color.GRAY);
        panel.add(simulationTimeField);

        // Etiqueta para "Start Time"
        JLabel startTimeLabel = new JLabel("Start Time:");
        startTimeLabel.setForeground(Color.GRAY);
        panel.add(startTimeLabel);

        // Campo de entrada de texto para "Start Time"
        startTimeField = new JTextField();
        startTimeField.setForeground(Color.GRAY);
        panel.add(startTimeField);

        // Botón para guardar cambios
        JButton saveButton = new JButton("Guardar Cambios");
        saveButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Agrega aquí la lógica para guardar los cambios
                String simulationTime = simulationTimeField.getText();
                String startTime = startTimeField.getText();
                // Procesa los valores ingresados

                controller.handleConfiguration(simulationTime, startTime);

                // Cierra la ventana
                dispose();
            }
        });

        // Establece el color de fondo en gris
        saveButton.setBackground(Color.GRAY);
        saveButton.setForeground(Color.WHITE);

        // Agrega el botón al panel
        panel.add(saveButton);

        // Agrega el panel a la ventana
        add(panel);

        // Hacer visible la ventana
        setVisible(true);

        // --------------------------------------------- Methods ---------------------------------------------
    }
}
