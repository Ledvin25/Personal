package Lyric;

import java.util.ArrayList;
import java.util.List;

public class LyricByGender {
    
    public class SalsaGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Salsa"; // Aqui iria toda la implementacion
        }
        
    }

    public class BachataGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Bachata"; // Aqui iria toda la implementacion
        }
        
    }

    public class MerengueGenerator extends LyricGenerator {
        
        @Override
        public String lyricGenerator(String[] frases) {
            return "Letra en version Merengue"; // Aqui iria toda la implementacion
        }
        
    }

    // Y asi con todos los generadores de letras por genero, no se me ocurre como hacerlo en una sola clase

    // Fusionar generos 

    public class GeneroFusionado extends LyricGenerator {
        private List<LyricGenerator> generosSeleccionados = new ArrayList<>();
    
        public void agregarGenero(LyricGenerator genero) {
            generosSeleccionados.add(genero);
        }
    
        @Override
        public String lyricGenerator(String[] frases) {
            for (LyricGenerator genero : generosSeleccionados) {
                // Genera letras para cada género seleccionado
            }
            return "Letra fusionada"; // Aqui iria toda la implementacion
        }
    }
}
