package gui;

import javax.swing.*;

import model.Stop;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NearbyStop extends JFrame{
    private JFrame frame;
    private JComboBox<String> stopComboBox;


    public NearbyStop(StopController stopController) {
        frame = new JFrame("Selección de Parada");
        frame.setSize(300, 550);
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
        stopComboBox.setPreferredSize(new Dimension(120, 30)); // Tamaño del ComboBox
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

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);
    }
}
