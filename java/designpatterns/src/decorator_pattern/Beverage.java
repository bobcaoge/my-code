package decorator_pattern;

public abstract class Beverage {
    protected String description;
    public String getDescription(){
        return this.description;
    }
    public double cost(){
        return 0;
    }
}
