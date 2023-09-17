package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NearbyStop {
    private JFrame frame;
    private JComboBox<String> stopComboBox;

    public NearbyStop() {
        frame = new JFrame("Selección de Parada");
        frame.setSize(200, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Panel para organizar componentes en el centro de la ventana
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        panel.setBorder(BorderFactory.createEmptyBorder(100, 50, 100, 50)); // Añadir espacio alrededor

        // Etiqueta de selección de parada
        JLabel stopLabel = new JLabel("Selecciona la Parada:");
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(0, 0, 10, 0); // Espacio inferior
        panel.add(stopLabel, gbc);

        // ComboBox para seleccionar la parada
        stopComboBox = new JComboBox<>(new String[]{"Stop1", "Stop2", "Stop3", "Stop4", "Stop5"});
        gbc.gridy = 1;
        gbc.ipadx = 50; // Ancho del ComboBox
        gbc.ipady = 20; // Alto del ComboBox
        gbc.insets = new Insets(0, 0, 10, 0); // Espacio inferior
        panel.add(stopComboBox, gbc);

        // Botón para confirmar la selección
        JButton seleccionarButton = new JButton("Seleccionar");
        seleccionarButton.setPreferredSize(new Dimension(120, 30)); // Tamaño del botón
        gbc.gridy = 2;
        gbc.ipadx = 0; // Restablecer el ancho del ComboBox
        gbc.ipady = 0; // Restablecer el alto del ComboBox
        gbc.insets = new Insets(10, 0, 0, 0); // Espacio superior
        panel.add(seleccionarButton, gbc);

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new NearbyStop();
            }
        });
    }
}
