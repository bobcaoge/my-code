package command_pattern.domain;

public class Stereo {
    private String name;
    public Stereo(String name){
        this.name = name;
    }
    public void on(){
        System.out.println("turn on the Stereo on " + this.name);
    }
    public void off(){
        System.out.println("turn off the Stereo on " + this.name);
    }
}
