package Player;

import Lyric.LyricByGender;
import Music.MusicByGender;

public class MusicPlayer {
    
    private LyricByGender lyricGenerator;
    private MusicByGender musicGenerator;

    public void setGender(String genero)
    {
        // Logica para escoger el genero
    }

    public void reproducirCancion (String[] frases)
    {
        String lyric = lyricGenerator.lyricGenerator(frases);
        String music = musicGenerator.musicGenerator(frases);
        // Logica para reproducir la cancion
    }

    public void addGenderFusion(String genero)
    {
        int maxGender = 1;
        int actualGender = 0;

        if (actualGender < maxGender)
        {
            // Logica para agregar el genero
            actualGender++;
        }
    }
}
