package adaptor_pattern;

public class Main {
    public static void main(String[] args) {
        Turkey turkey = new WildTurkey();
        Duck duck = new YellowDuck();
        AdaptorDuck adaptorDuck = new AdaptorDuck(turkey);

        test(duck);
        test(adaptorDuck);
    }
        public static void test(Duck duck){
        duck.quack();
        duck.fly();
    }
}
