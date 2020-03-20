package state_pattern;


public class Sold implements State{
    private GumballMachine gumballMachine;
    public Sold(GumballMachine gumballMachine){
        this.gumballMachine = gumballMachine;
    }

    @Override
    public void insertQuarter() {
        System.out.println("please wait, we're already giving you a gumball");
    }

    @Override
    public void ejectQuarter() {
        System.out.println("Sorry, you already turned the crank");

    }

    @Override
    public void turnCrank() {
        System.out.println("turning twice doesn't get you another gumball");

    }

    @Override
    public void dispense() {
        System.out.println("A gumball comes rolling out the slot!");
        gumballMachine.minusCount();
        if(gumballMachine.getCount() == 0){
            System.out.println("Oops, out of gumballs");
            gumballMachine.setState(gumballMachine.getSoldOut());
        }else {
            gumballMachine.setState(gumballMachine.getNoQuarter());
        }
    }
}
