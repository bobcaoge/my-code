package command_pattern.domain;

public class CeilingFan {
    private String name;
    public CeilingFan(String name){
        this.name = name;
    }
    public void on(){
        System.out.println("turn on the ceiling fan on " + this.name);
    }
    public void off(){
        System.out.println("turn off the ceiling fan on " + this.name);
    }
}
