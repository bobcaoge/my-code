package iterator_pattern;

import java.util.ArrayList;

public class ArrayListMenuIterator implements Iterator{
    ArrayList<MenuItem> menuItems;
    int pos = 0;
    public ArrayListMenuIterator(ArrayList menuItems){
        this.menuItems = menuItems;
    }
    @Override

    public boolean hasNext() {
        return pos < menuItems.size();
    }

    @Override
    public MenuItem Next() {
        return hasNext() ? menuItems.get(pos++) : null;
    }
}
