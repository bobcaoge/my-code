package singleton_pattern;

public class Main {
    public static void main(String[] args) {
        Myclass obj = Myclass.getObject();
        System.out.println(obj.getS());
    }
}
