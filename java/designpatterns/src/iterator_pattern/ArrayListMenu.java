package iterator_pattern;

import java.io.FileReader;
import java.util.ArrayList;

public class ArrayListMenu implements Menu{
    ArrayList<MenuItem> menuItems;
    public ArrayListMenu(){
        menuItems = new ArrayList<>();
        for (int i = 0; i < 9 ; i++) {
            menuItems.add(new MenuItem("a"+i, i+3));
        }
    }
    @Override
    public Iterator createIterator(){
        return new ArrayListMenuIterator(menuItems);
    }
}
