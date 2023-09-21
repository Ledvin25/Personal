package Player;

import Lyric.LyricByGender;
import Music.MusicByGender;

public class MusicPlayer {

    LyricByGender lyricGenerator = new LyricByGender();
        LyricByGender.SalsaGenerator salsaGenerator = lyricGenerator.new SalsaGenerator();
        LyricByGender.BachataGenerator bachataGenerator = lyricGenerator.new BachataGenerator();
        // Y asi con todos los generadores de letras por genero

        MusicByGender musicGenerator = new MusicByGender();
        MusicByGender.SalsaMusic salsaMusic = musicGenerator.new SalsaMusic();
        MusicByGender.BachataMusic bachataMusic = musicGenerator.new BachataMusic();
        // Y asi con todos los generadores de musica por genero

    public void setGender(String genero)
    {
        // Logica para escoger el genero
    }

    public void reproducirCancion (String[] frases)
    {

        // Switch para escoger el genero

        String opcion = "Salsa";

        switch (opcion)
        {
            case "Salsa":
                salsaGenerator.lyricGenerator(frases);
                salsaMusic.musicGenerator(frases);
                // Logica para reproducir la cancion
                break;
            case "Bachata":
                System.out.println("Bachata");
                break;
            case "Merengue":
                System.out.println("Merengue");
                break;
            default:
                System.out.println("No se ha seleccionado un genero");
                break;
        }

    }

    public void addGenderFusion(String genero)
    {
        int maxGender = 1;
        int actualGender = 0;
        MusicByGender.GeneroFusionado generoFusionado = musicGenerator.new GeneroFusionado();
        LyricByGender.GeneroFusionado generoFusionadoLyric = lyricGenerator.new GeneroFusionado();

        while (actualGender < maxGender)
        {
            String opcionFusion = "Salsa";

            switch (opcionFusion)
            {
                case "Salsa":
                // Faltaria alguna logica para que no se pueda repetir el genero
                    generoFusionado.agregarGenero(salsaMusic);
                    generoFusionadoLyric.agregarGenero(salsaGenerator);
                    break;
                case "Bachata":
                    generoFusionado.agregarGenero(bachataMusic);
                    generoFusionadoLyric.agregarGenero(bachataGenerator);
                    break;
                case "Merengue":
                    System.out.println("Merengue");
                    break;
                default:
                    System.out.println("No se ha seleccionado un genero");
                    break;
            }
            actualGender++;
        }
    }
}
