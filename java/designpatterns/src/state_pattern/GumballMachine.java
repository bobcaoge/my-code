package state_pattern;

public class GumballMachine {
    private NoQuarter noQuarter;
    private HasQuarter hasQuarter;
    private Sold sold;
    private SoldOut soldOut;
    private State state;
    private int count = 0;
    public GumballMachine(){
        noQuarter = new NoQuarter(this);
        hasQuarter = new HasQuarter(this);
        sold = new Sold(this);
        soldOut = new SoldOut(this);
        state = noQuarter;
        count = 10;
    }

    public int getCount() {
        return count;
    }
    public void minusCount(){
        this.count--;
    }

    public HasQuarter getHasQuarter() {
        return hasQuarter;
    }

    public NoQuarter getNoQuarter() {
        return noQuarter;
    }

    public Sold getSold() {
        return sold;
    }

    public SoldOut getSoldOut() {
        return soldOut;
    }

    public void setState(State state){
        this.state = state;

    }
    public void insertQuarter() {
        state.insertQuarter();
    }

    public void ejectQuarter() {
        state.ejectQuarter();
    }

    public void turnCrank() {
        state.turnCrank();
    }

    public void dispense() {
        state.dispense();
    }

}
