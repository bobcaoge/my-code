package adaptor_pattern;

public class YellowDuck implements Duck{
    @Override
    public void quack() {
        System.out.println("gua gua gua");
    }

    @Override
    public void fly() {
        System.out.println("flying");
    }
}
