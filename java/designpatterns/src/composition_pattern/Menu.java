package composition_pattern;

import java.util.ArrayList;
import java.util.Iterator;

public class Menu extends MenuComponent{
    ArrayList<MenuComponent> children;
    public Menu(){
        this.children = new ArrayList<>();
    }
    @Override
    public void add(MenuComponent component) throws UnsupportedOperationException {
        this.children.add(component);
    }
    public Iterator createIterator(){
        return new MenuCompositeIterator(this);
    }
}
