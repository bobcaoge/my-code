package composition_pattern;

public abstract class MenuComponent {
    public void add(MenuComponent component) throws UnsupportedOperationException{
        throw new UnsupportedOperationException();
    }
    public void remove(MenuComponent component) throws UnsupportedOperationException{
        throw new UnsupportedOperationException();
    }

}
