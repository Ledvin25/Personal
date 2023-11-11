package Paints;

import java.util.List;

public class AbstractPaintingIterator implements Iterator {

  private List<ShapeStrategy> shapes;
  private int position;

  public AbstractPaintingIterator(List<ShapeStrategy> shapes) {
    this.shapes = shapes;
  }

  public boolean hasNext() {
    return position < shapes.size();
  }

  public ShapeStrategy next() {
    return shapes.get(position++); 
  }

}
