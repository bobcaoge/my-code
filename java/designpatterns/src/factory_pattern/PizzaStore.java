package factory_pattern;

public abstract class PizzaStore {
    public abstract Pizza creatPizza(String type);
    public Pizza orderPizza(String type){
        Pizza pizza = null;
        pizza = creatPizza(type);
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        return pizza;
    }

}
