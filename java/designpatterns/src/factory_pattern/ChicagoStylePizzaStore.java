package factory_pattern;

public class ChicagoStylePizzaStore extends PizzaStore{
    @Override
    public Pizza creatPizza(String type) {
        Pizza pizza = null;
        if (type.equals("cheese")){
            pizza = new ChicagoStyleCheesePizza();
        }else if (type.equals("clam")){
            pizza = new ChicagoStyleClamPizza();
        }else if (type.equals("pepperoni")){
            pizza = new ChicagoStylePepperoniPizza();
        }else if(type.equals("veggie")){
            pizza = new ChicagoStyleVeggiePizza();
        }
        return pizza;
    }
}
