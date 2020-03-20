package factory_pattern;


public class Pizza {
    String name;
    String sauce;
    String dough;

    public void prepare(){
        System.out.println("preparing " + name);
    }

    public void bake(){
        System.out.println("baking");
    }
    public void cut(){
        System.out.println("cutting");
    }
    public void box(){
        System.out.println("place in official box");
    }

    public String getName(){
        return this.name;
    }
}
