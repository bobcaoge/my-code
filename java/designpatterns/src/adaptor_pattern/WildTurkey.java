package adaptor_pattern;

public class WildTurkey implements Turkey{
    @Override
    public void fly() {
        System.out.println("flying");
    }

    @Override
    public void goggle() {
        System.out.println("ge ge ge");
    }
}
