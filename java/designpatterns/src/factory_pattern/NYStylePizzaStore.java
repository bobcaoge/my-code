package factory_pattern;

public class NYStylePizzaStore extends PizzaStore{
    @Override
    public Pizza creatPizza(String type) {
        Pizza pizza = null;
        if (type.equals("cheese")){
            pizza = new NYStyleCheesePizza();
        }else if (type.equals("clam")){
            pizza = new NYStyleClamPizza();
        }else if (type.equals("pepperoni")){
            pizza = new NYStylePepperoniPizza();
        }else if(type.equals("veggie")){
            pizza = new NYStyleVeggiePizza();
        }
        return pizza;
    }
}
