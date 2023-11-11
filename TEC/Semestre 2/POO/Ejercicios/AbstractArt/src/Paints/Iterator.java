package Paints;

import Painters.PainterStrategy;

public interface Iterator {
    boolean hasNext();
    PainterStrategy next(); 
}
