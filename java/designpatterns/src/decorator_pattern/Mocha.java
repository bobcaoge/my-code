package decorator_pattern;

public class Mocha extends Beverage{
    private Beverage beverage;
    public Mocha(Beverage beverage){
        this.beverage = beverage;
    }

    @Override
    public String getDescription() {
        return this.beverage.getDescription()+", mocha";
    }

    @Override
    public double cost() {
        return this.beverage.cost() + 0.20;
    }
}
