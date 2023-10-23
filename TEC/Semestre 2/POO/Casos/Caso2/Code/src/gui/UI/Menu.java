package gui.UI;

import javax.swing.*;

import gui.Controllers.MenuController;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Menu extends JFrame {

    private MenuController controller;

    public Menu(MenuController controller) {

        this.controller = controller;

        // Configura la ventana
        setSize(500, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Crea un panel para colocar los botones en el centro
        JPanel buttonPanel = new JPanel(new GridLayout(5, 1, 0, 15));
        buttonPanel.setBorder(BorderFactory.createEmptyBorder(0, 50, 0, 50));

        // Crea los botones
        JButton iniciarButton = createButton("Iniciar", Color.BLACK, 14);
        JButton guardarButton = createButton("Guardar", Color.DARK_GRAY, 14);
        JButton cargarButton = createButton("Cargar", Color.DARK_GRAY, 14);
        JButton configuracionButton = createButton("Configuración", Color.DARK_GRAY, 14);
        JButton salirButton = createButton("Salir", Color.BLACK, 14);

        // Agrega los botones al panel
        buttonPanel.add(iniciarButton);
        buttonPanel.add(guardarButton);
        buttonPanel.add(cargarButton);
        buttonPanel.add(configuracionButton);
        buttonPanel.add(salirButton);

        // Crea un panel para el encabezado
        JPanel headerPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JLabel headerLabel = new JLabel("Menú");
        headerPanel.add(headerLabel);

        // Crea un panel para el pie de página
        JPanel footerPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JLabel footerLabel = new JLabel("Made by Ledvin");
        footerPanel.add(footerLabel);

        // Agrega los paneles a la ventana
        add(headerPanel, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.CENTER);
        add(footerPanel, BorderLayout.SOUTH);

        // Muestra la ventana
        setVisible(true);
    }

    private JButton createButton(String text, Color color, int fontSize) {
        JButton button = new JButton(text);
        button.setBackground(color);
        button.setForeground(Color.WHITE);
        button.setFocusPainted(false);
        button.setFont(new Font("Arial", Font.PLAIN, fontSize));

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Maneja las acciones de los botones
                if (text.equals("Iniciar")) {
                    // Código para la opción "Iniciar"
                    controller.handleStart();

                    // Cerrar la ventana
                    setVisible(false);
                    dispose();

                } else if (text.equals("Guardar")) {
                    // Código para la opción "Guardar"
                    controller.handleSave();
                } else if (text.equals("Cargar")) {
                    // Código para la opción "Cargar"

                    controller.handleLoad();
                } else if (text.equals("Configuración")) {
                    // Código para la opción "Configuración"

                    controller.handleConfig();
                } else if (text.equals("Salir")) {
                    System.exit(0);
                }
            }
        });

        return button;
    }
}
