package Factory;

import Painters.PainterStrategy;

public interface PainterFactory {
    PainterStrategy createPainter(int red, int blue, int green, int priority);
}
