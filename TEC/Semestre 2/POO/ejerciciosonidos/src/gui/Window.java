package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import sounds.SoundBoard;

public class Window {

    private static String sound1 = "sound1.wav";
    private static String sound2 = "sound2.wav";
    private static String sound3 = "sound3.wav";
    private static String sound4 = "sound4.wav";
    private static String sound5 = "sound5.wav";
    private static String sound6 = "sound6.wav";

    public static void main(String[] args) {

        SoundBoard soundBoard = new SoundBoard();

        JFrame frame = new JFrame("DJ Soundboard");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        JPanel mainPanel = new JPanel(new BorderLayout());

        JButton editarButton = new JButton("Editar");

        JPanel panel = new JPanel(new GridLayout(2, 3));

        JButton boton1 = new JButton("Sonido 1");
        JButton boton2 = new JButton("Sonido 2");
        JButton boton3 = new JButton("Sonido 3");
        JButton boton4 = new JButton("Sonido 4");
        JButton boton5 = new JButton("Sonido 5");
        JButton boton6 = new JButton("Sonido 6");

        panel.add(boton1);
        panel.add(boton2);
        panel.add(boton3);
        panel.add(boton4);
        panel.add(boton5);
        panel.add(boton6);

        mainPanel.add(editarButton, BorderLayout.NORTH);
        mainPanel.add(panel, BorderLayout.CENTER);

        frame.getContentPane().add(mainPanel);

        frame.setVisible(true);

        editarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Mostrar una ventana emergente para la edición
                JPanel editPanel = new JPanel(new GridLayout(3, 1));
                JComboBox<String> botonComboBox = new JComboBox<>(new String[]{"Botón 1", "Botón 2", "Botón 3", "Botón 4", "Botón 5", "Botón 6"});
                JTextField nombreTextField = new JTextField();
                JButton guardarButton = new JButton("Guardar");

                editPanel.add(botonComboBox);
                editPanel.add(nombreTextField);
                editPanel.add(guardarButton);

                int result = JOptionPane.showConfirmDialog(frame, editPanel, "Editar", JOptionPane.OK_CANCEL_OPTION);
                if (result == JOptionPane.OK_OPTION) {
                    String selectedButton = (String) botonComboBox.getSelectedItem();
                    String nuevoNombre = nombreTextField.getText();
                    actualizarVariable(selectedButton, nuevoNombre);
                }
            }
        });

        // Agregar ActionListener a los botones
        boton1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound1);
            }
        });
        boton2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound2);
            }
        });
        boton3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound3);
            }
        });
        boton4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound4);
            }
        });
        boton5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound5);
            }
        });
        boton6.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                soundBoard.sound(sound6);
            }
        });
    }

    private static void actualizarVariable(String selectedButton, String nuevoNombre) {
        // Actualizar la variable correspondiente según el botón seleccionado
        switch (selectedButton) {
            case "Botón 1":
                sound1 = nuevoNombre;
                break;
            case "Botón 2":
                sound2 = nuevoNombre;
                break;
            case "Botón 3":
                sound3 = nuevoNombre;
                break;
            case "Botón 4":
                sound4 = nuevoNombre;
                break;
            case "Botón 5":
                sound5 = nuevoNombre;
                break;
            case "Botón 6":
                sound6 = nuevoNombre;
                break;
        }
    }
}
