package singleton_pattern;

public class Myclass {
    private static volatile Myclass obj;
    private String s = "I am the only instance of the class";
    private Myclass(){};
    public static Myclass getObject(){
        if (obj == null){
            synchronized (Myclass.class) {
                if (obj == null) {
                    obj = new Myclass();
                }
            }
        }
        return obj;
    }
    /**
     * 线程不安全
     */
//    public static Myclass getObject(){
//        if (obj == null){
//            obj = new Myclass();
//        }
//        return obj;
//    }
    public String getS(){
        return s;
    }
}

