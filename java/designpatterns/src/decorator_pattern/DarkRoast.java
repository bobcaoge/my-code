package decorator_pattern;

public class DarkRoast extends Beverage{
    public DarkRoast(){
        description = "dark roast";
    }

    @Override
    public double cost() {
        return 0.99;
    }
}
