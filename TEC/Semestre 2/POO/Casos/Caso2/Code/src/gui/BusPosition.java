package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BusPosition {
    private JFrame frame;
    private JTextArea consoleTextArea;
    private JButton previousBusButton;
    private JButton getInfoButton;
    private JButton nextBusButton;

    public BusPosition() {
        // Crear la ventana principal
        frame = new JFrame("Bus Position");
        frame.setSize(500, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Crear el panel principal con un BorderLayout
        JPanel mainPanel = new JPanel(new BorderLayout());
        frame.add(mainPanel);

        // Crear el área de la consola (JTextArea) y colocarlo en un JScrollPane
        consoleTextArea = new JTextArea();
        consoleTextArea.setEditable(false); // Hacer que el área de la consola sea de solo lectura
        JScrollPane scrollPane = new JScrollPane(consoleTextArea);
        mainPanel.add(scrollPane, BorderLayout.CENTER);

        // Crear el panel inferior para los botones
        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        bottomPanel.setBackground(Color.decode("#bdffa1")); // Cambiar el color de fondo
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        // Crear los botones
        previousBusButton = new JButton("Bus Anterior");
        previousBusButton.setBackground(Color.decode("#ff6b6b"));
        getInfoButton = new JButton("Obtener Info");
        getInfoButton.setBackground(Color.decode("#ff6b6b"));
        nextBusButton = new JButton("Bus Siguiente");
        nextBusButton.setBackground(Color.decode("#ff6b6b"));

        // Agregar los botones al panel inferior
        bottomPanel.add(previousBusButton);
        bottomPanel.add(getInfoButton);
        bottomPanel.add(nextBusButton);

        // Hacer visible la ventana
        frame.setVisible(true);

        // Agregar ActionListener a los botones
        previousBusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Lógica para mostrar la acción del botón "Bus Anterior" en la consola
                consoleTextArea.append("Accion\n");
            }
        });

        getInfoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Lógica para mostrar la acción del botón "Obtener Info" en la consola
                consoleTextArea.append("Accion\n");
            }
        });

        nextBusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Lógica para mostrar la acción del botón "Bus Siguiente" en la consola
                consoleTextArea.append("Accion\n");
            }
        });
    }

    public static void main(String[] args) {
        // Crear la ventana de la consola de posición del autobús
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new BusPosition();
            }
        });
    }
}
