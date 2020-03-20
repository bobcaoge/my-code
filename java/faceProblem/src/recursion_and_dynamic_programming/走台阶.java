package recursion_and_dynamic_programming;

public class 走台阶 {
    public static int get(int n){
        if (n == 1){
            return 1;
        }
        if (n == 2){
            return 2;
        }
        return get(n-1)+get(n-2);
    }
}
