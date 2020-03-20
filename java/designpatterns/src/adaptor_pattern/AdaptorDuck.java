package adaptor_pattern;

public class AdaptorDuck implements Duck{
    Turkey turkey;
    public AdaptorDuck(Turkey turkey){
        this.turkey = turkey;
    }

    @Override
    public void quack() {
        this.turkey.goggle();
    }

    @Override
    public void fly() {
        this.turkey.fly();
    }
}
