package composition_pattern;

import iterator_pattern.Iterator;

public class NoIterator implements Iterator {
    @Override
    public Object Next() {
        return null;
    }

    @Override
    public boolean hasNext() {
        return false;
    }
}
