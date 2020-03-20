package command_pattern.domain;

public class GarageDoor {
    private String name;
    public GarageDoor(String name){
        this.name = name;
    }
    public void on(){
        System.out.println("turn on the Garage door ");
    }
    public void off(){
        System.out.println("turn off the Garage door ");
    }
}
