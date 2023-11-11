package gui.UI;

import javax.swing.*;

import gui.Controllers.StopController;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NearbyStop extends JFrame{
    private JFrame frame;
    private JComboBox<String> stopComboBox;


    public NearbyStop(StopController stopController) {
        frame = new JFrame("Selección de Parada");
        frame.setSize(700, 550);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Panel para organizar componentes en el centro de la ventana
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        panel.setBackground(Color.decode("#bdffa1")); // Cambio de color de fondo
        panel.setBorder(BorderFactory.createEmptyBorder(100, 50, 100, 50)); // Añadir espacio alrededor

        // Etiqueta de selección de parada
        JLabel stopLabel = new JLabel("Seleccione la parada:");
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(0, 0, 10, 0); // Espacio inferior
        panel.add(stopLabel, gbc);

        // ComboBox para seleccionar la parada
        stopComboBox = new JComboBox<>(stopController.getStopList());
        stopComboBox.setPreferredSize(new Dimension(500, 50)); // Tamaño del ComboBox
        stopComboBox.setBackground(Color.decode("#ff887d")); // Cambio de color del ComboBox
        stopComboBox.setForeground(Color.BLACK); // Cambio de color del texto del ComboBox
        gbc.gridy = 1;
        gbc.insets = new Insets(0, 0, 10, 0); // Espacio inferior
        panel.add(stopComboBox, gbc);

        // Botón para confirmar la selección
        JButton seleccionarButton = new JButton("Seleccionar");
        seleccionarButton.setPreferredSize(new Dimension(120, 30)); // Tamaño del botón
        seleccionarButton.setBackground(Color.decode("#ff6b6b")); // Cambio de color de fondo del botón
        seleccionarButton.setForeground(Color.WHITE); // Cambio de color del texto del botón
        seleccionarButton.setBorder(BorderFactory.createLineBorder(Color.BLACK)); // Borde negro
        gbc.gridy = 2;
        gbc.insets = new Insets(10, 0, 0, 0); // Espacio superior
        panel.add(seleccionarButton, gbc);

        // Agregar un manejador de eventos al botón "Seleccionar"
        seleccionarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Obtener la parada seleccionada del ComboBox
                String selectedStop = (String) stopComboBox.getSelectedItem();

                // Llamar a la función del controlador
                stopController.getSelectedStop(selectedStop);

                // Cerrar la ventana

                frame.setVisible(false);
                frame.dispose();
            }
        });

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);
    }
}