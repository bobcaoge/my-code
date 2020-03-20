package state_pattern;

public class HasQuarter implements State{
    private GumballMachine gumballMachine;
    public HasQuarter(GumballMachine gumballMachine){
        this.gumballMachine = gumballMachine;
    }
    @Override
    public void insertQuarter() {
        System.out.println("you can't insert another quarter");
    }

    @Override
    public void ejectQuarter() {
        System.out.println("ejected a quarter");
        gumballMachine.setState(gumballMachine.getNoQuarter());
    }

    @Override
    public void turnCrank() {
        System.out.println("you turned ...");
        gumballMachine.setState(gumballMachine.getNoQuarter());
    }

    @Override
    public void dispense() {
        System.out.println("No gumball dispense");
    }
}
