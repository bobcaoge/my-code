package factory_pattern;

public class Main {
    public static void main(String[] args) {
        PizzaStore pizzaStore = new NYStylePizzaStore();
        pizzaStore.orderPizza("cheese");

        pizzaStore = new ChicagoStylePizzaStore();
        pizzaStore.orderPizza("veggie");
    }
}
