package Music;

public class MusicByGender {

    class SalsaMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Salsa"; // Aqui iria toda la implementacion
        }
        
    }

    class BachataMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Bachata"; // Aqui iria toda la implementacion
        }
        
    }

    class MerengueMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Merengue"; // Aqui iria toda la implementacion
        }
        
    }

    // Y asi con todos los generadores de letras por genero, no se me ocurre como hacerlo en una sola clase
}
