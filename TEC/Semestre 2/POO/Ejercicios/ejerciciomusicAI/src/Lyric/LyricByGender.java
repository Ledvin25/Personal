package Lyric;

public class LyricByGender {
    
    class SalsaGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Salsa"; // Aqui iria toda la implementacion
        }
        
    }

    class BachataGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Bachata"; // Aqui iria toda la implementacion
        }
        
    }

    class MerengueGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Merengue"; // Aqui iria toda la implementacion
        }
        
    }

    // Y asi con todos los generadores de letras por genero, no se me ocurre como hacerlo en una sola clase
}
