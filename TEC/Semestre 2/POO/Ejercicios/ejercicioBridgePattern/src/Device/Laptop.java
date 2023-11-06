package Device;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.FloatControl;

public class Laptop implements DeviceBridge
{

    private String relacionAspecto;

    public Laptop() {
        this.relacionAspecto = "16:9";
    }
    public String getRelacionAspecto() {
        return relacionAspecto;
    }

    public void reproducirSonido(int volumen) {
        try {
            // Cargar el archivo de sonido
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(Laptop.class.getResource("sound1.wav"));
    
            // Obtener la línea de clip de audio
            Clip clip = AudioSystem.getClip();
    
            // Abrir la línea de clip de audio con el archivo de sonido
            clip.open(audioInputStream);
    
            // Obtener el control de volumen
            FloatControl control = (FloatControl) clip.getControl(FloatControl.Type.MASTER_GAIN);
    
            // Establecer el volumen (en decibelios, de -80 a 6)
            float gain = (float) (20 * Math.log10((double) volumen / 100));
            control.setValue(gain);
    
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
