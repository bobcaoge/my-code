package decorator_pattern;

public class Main {
    public static void main(String[] args) {
        Beverage coffee = new DarkRoast();
        coffee = new Mocha(coffee);
        coffee = new Soy(coffee);
        coffee = new Whip(coffee);
        System.out.println(coffee.getDescription());
        System.out.println(coffee.cost());
    }
}
