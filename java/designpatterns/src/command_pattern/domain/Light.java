package command_pattern.domain;

public class Light {
    private String name;
    public Light(String name){
    this.name = name;
    }
    public void on(){
        System.out.println("turn on the light on " + this.name);
    }
    public void off(){
        System.out.println("turn off the light on " + this.name);
    }
}
