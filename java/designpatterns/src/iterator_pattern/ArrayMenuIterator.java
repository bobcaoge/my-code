package iterator_pattern;

public class ArrayMenuIterator implements Iterator{
    private MenuItem[] menuItems;
    private int pos = 0;
    public ArrayMenuIterator(MenuItem[] menuItems){
        this.menuItems = menuItems;
    }
    @Override
    public MenuItem Next() {
        return hasNext() ? menuItems[pos++] : null;
    }

    @Override
    public boolean hasNext() {
        return pos<menuItems.length;
    }
}
