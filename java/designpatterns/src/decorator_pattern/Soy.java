package decorator_pattern;

public class Soy extends Beverage{
    private Beverage beverage;
    public Soy(Beverage beverage){
        this.beverage = beverage;
    }

    @Override
    public String getDescription() {
        return this.beverage.getDescription() + ", soy";
    }

    @Override
    public double cost() {
        return this.beverage.cost() + 0.3;
    }
}
