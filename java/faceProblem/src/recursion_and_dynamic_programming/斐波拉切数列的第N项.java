package recursion_and_dynamic_programming;

public class 斐波拉切数列的第N项 {
    public static int get_Nth(int n){
        if (n==1){
            return 1;
        }
        if (n == 2){
            return 1;
        }
        return get_Nth(n-1)+get_Nth(n-2);
    }
    public static int get_Nth_2(int n){
        int a = 1;
        int b = 1;
        for (int i=0;i<n;i++){
            int temp = a;
            a = a+b;
            b = temp;
        }
        return a;
    }


}
