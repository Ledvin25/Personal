package Music;

import java.util.ArrayList;
import java.util.List;

public class MusicByGender {

    public class SalsaMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Salsa"; // Aqui iria toda la implementacion
        }
        
    }

    public class BachataMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Bachata"; // Aqui iria toda la implementacion
        }
        
    }

    public class MerengueMusic extends MusicGenerator {
        
        @Override
        public String musicGenerator(String[] frases) {
            return "Musica en version Merengue"; // Aqui iria toda la implementacion
        }
        
    }

    // Fusionar generos
    public class GeneroFusionado extends MusicGenerator {
        private List<MusicGenerator> generosSeleccionados = new ArrayList<>();
    
        public void agregarGenero(MusicGenerator genero) {
            generosSeleccionados.add(genero);
        }
    
        @Override
        public String musicGenerator(String[] frases) {
            for (MusicGenerator genero : generosSeleccionados) {
                // Genera música para cada género seleccionado
            }
            return "Musica fusionada"; // Aqui iria toda la implementacion
        }
    }

    // Y asi con todos los generadores de letras por genero, no se me ocurre como hacerlo en una sola clase
}
