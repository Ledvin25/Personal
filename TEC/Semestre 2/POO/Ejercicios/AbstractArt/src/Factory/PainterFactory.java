package Factory;

import Painters.PainterStrategy;

public interface PainterFactory {
    PainterStrategy createPainter();
}
