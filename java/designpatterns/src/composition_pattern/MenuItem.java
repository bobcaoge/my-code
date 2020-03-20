package composition_pattern;


import iterator_pattern.Iterator;

public class MenuItem extends MenuComponent{
    int price;
    String name;
    public MenuItem(int price, String name){
        this.price = price;
        this.name = name;
    }

    public Iterator createIterator(){
        return new NoIterator();
    }

    @Override
    public String toString() {
        return this.name+" "+this.price;
    }
}
