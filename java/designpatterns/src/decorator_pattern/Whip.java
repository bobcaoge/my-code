package decorator_pattern;

public class Whip extends Beverage{
    private Beverage beverage;
    public Whip(Beverage beverage){
        this.beverage = beverage;
    }

    @Override
    public String getDescription() {
        return this.beverage.getDescription()+", whip";
    }

    @Override
    public double cost() {
        return this.beverage.cost() + 0.1;
    }
}
