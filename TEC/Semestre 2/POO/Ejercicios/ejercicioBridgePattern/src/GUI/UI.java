package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import Control.*;
import Device.*;

public class UI extends JFrame {
    JComboBox<String> comboBox;
    JLabel pantallaImagen;
    JButton botonProyectar;
    JButton botonReproducir;
    JSlider sliderVolumen;

    DeviceBridge laptop = new Laptop();
    DeviceBridge tv = new TV();
    DeviceBridge smartphone = new Smartphone();
    DeviceControl googleHome = new GoogleHome();

    public UI() {
        setTitle("Control de Dispositivos");
        setSize(700, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());

        // ComboBox para seleccionar dispositivo
        comboBox = new JComboBox<>(new String[]{"Smartphone", "Laptop", "SmartTV"});
        panel.add(comboBox, BorderLayout.NORTH);

        // Panel para la imagen
        JPanel panelImagen = new JPanel();
        panelImagen.setBackground(Color.WHITE);
        pantallaImagen = new JLabel("");
        pantallaImagen.setHorizontalAlignment(SwingConstants.CENTER);
        pantallaImagen.setVerticalAlignment(SwingConstants.CENTER);
        pantallaImagen.setPreferredSize(new Dimension(500, 300));
        panelImagen.add(pantallaImagen);
        panel.add(panelImagen, BorderLayout.CENTER);

        // Botón para proyectar imagen
        botonProyectar = new JButton("Proyectar");
        panel.add(botonProyectar, BorderLayout.LINE_START);

        // Controles de volumen
        sliderVolumen = new JSlider(0, 100, 50);
        panel.add(sliderVolumen, BorderLayout.LINE_END);

        // Botón para reproducir sonido
        botonReproducir = new JButton("Reproducir sonido");
        panel.add(botonReproducir, BorderLayout.SOUTH);

        add(panel);

        botonProyectar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String selectedDevice = comboBox.getSelectedItem().toString();
                int width = 0;
                int height = 0;
                switch (selectedDevice) {
                    case "Laptop":
                        googleHome.setDeviceBridge(laptop);
                        break;
                    case "Smartphone":
                        googleHome.setDeviceBridge(smartphone);
                        break;
                    case "SmartTV":
                        googleHome.setDeviceBridge(tv);
                        break;
                    default:
                        break;
                }
                String aspectRatio = googleHome.getImageSize();
                if (aspectRatio.equals("16:9")) {
                    width = 400;
                    height = 225;
                } else if (aspectRatio.equals("9:16")) {
                    width = 225;
                    height = 400;
                } else if (aspectRatio.equals("14:6")) {
                    width = 300;
                    height = 171;
                }
                ImageIcon image = new ImageIcon("D:\\System\\Desktop\\ejercicioBridgePattern\\src\\GUI\\meme.png");
                Image scaledImage = image.getImage().getScaledInstance(width, height, Image.SCALE_SMOOTH);
                ImageIcon scaledIcon = new ImageIcon(scaledImage);
                pantallaImagen.setIcon(scaledIcon);
            }
        });

        botonReproducir.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                switch (comboBox.getSelectedItem().toString()) {
                    case "Laptop":
                        googleHome.setDeviceBridge(laptop);
                        googleHome.reproducirSonido(sliderVolumen.getValue());
                        break;
                    case "Smartphone":
                        googleHome.setDeviceBridge(smartphone);
                        googleHome.reproducirSonido(sliderVolumen.getValue());
                        break;
                    case "SmartTV":
                        googleHome.setDeviceBridge(tv);
                        googleHome.reproducirSonido(sliderVolumen.getValue());
                        break;
                    default:
                        break;
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                UI ventana = new UI();
                ventana.setVisible(true);
            }
        });
    }
}
