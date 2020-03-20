package iterator_pattern;

public class MenuItem {
    private String name;
    private int price;
    public MenuItem(String name, int price){
        this.name = name;
        this.price = price;
    }

    @Override
    public String toString() {
        return this.name+" "+price;
    }
}
