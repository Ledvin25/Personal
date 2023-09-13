package sounds;

import javax.sound.sampled.*;

public class SoundBoard {

    public void sound(String soundName) {
        try {
            // Cargar el archivo de sonido
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(SoundBoard.class.getResource(soundName));

            // Obtener la línea de clip de audio
            Clip clip = AudioSystem.getClip();

            // Abrir la línea de clip de audio con el archivo de sonido
            clip.open(audioInputStream);

            // Reproducir el sonido
            clip.start();

            // Esperar hasta que termine de reproducirse el sonido
            Thread.sleep(clip.getMicrosecondLength() / 1000);

            // Cerrar la línea de clip de audio
            clip.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
