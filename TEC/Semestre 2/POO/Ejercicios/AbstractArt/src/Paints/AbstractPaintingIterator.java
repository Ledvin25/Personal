package Paints;

import java.util.List;

import Painters.PainterStrategy;

public class AbstractPaintingIterator implements Iterator {

  private List<PainterStrategy> shapes;
  private int position;

  public AbstractPaintingIterator(List<PainterStrategy> shapes) {
    this.shapes = shapes;
  }

  public boolean hasNext() {
    return position < shapes.size();
  }

  public PainterStrategy next() {
    return shapes.get(position++); 
  }

}
