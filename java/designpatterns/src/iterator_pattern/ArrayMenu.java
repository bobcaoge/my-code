package iterator_pattern;

import java.util.ArrayList;

public class ArrayMenu implements Menu{
    MenuItem[] menuItems;
    public ArrayMenu(){
        menuItems = new MenuItem[10];
        for (int i = 0; i < 9 ; i++) {
            menuItems[i] = new MenuItem("a"+i, i+3);
        }
    }
    @Override
    public Iterator createIterator(){
        return new ArrayMenuIterator(menuItems);
    }

}
