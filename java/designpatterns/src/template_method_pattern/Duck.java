package template_method_pattern;

public class Duck implements Comparable{
    float weight;
    String name;
    public Duck(String name, float weight){
        this.weight = weight;
        this.name = name;
    }
    @Override
    public int compareTo(Object o) {
        Duck another_duck = (Duck)o;
        if (this.weight < another_duck.weight){
            return -1;
        }else if(this.weight > another_duck.weight){
            return 1;
        }
        return 0;
    }

    @Override
    public String toString() {
        return this.name+" " +this.weight;
    }
}
