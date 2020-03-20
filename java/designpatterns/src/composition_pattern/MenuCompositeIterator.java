package composition_pattern;

import java.util.Iterator;
import java.util.Stack;

public class MenuCompositeIterator implements Iterator {
    Stack<Object> stack = new Stack<>();
    public MenuCompositeIterator(MenuComponent menuComponent){
        this.stack.push(menuComponent);
    }
    @Override
    public boolean hasNext() {
        if (this.stack.empty()){
            return false;
        }
        Iterator iterator = (Iterator) stack.peek();
        if (!iterator.hasNext()){
            stack.pop();
            return hasNext();
        }
        return true;
    }

    @Override
    public Object next() {
        if (hasNext()){
            Iterator iterator = (Iterator)stack.peek();
            MenuComponent component = (MenuComponent)stack.peek();
            if (iterator.hasNext()){
                stack.push(iterator.next());
            }
            return component;
        }
        return null;
    }
}











