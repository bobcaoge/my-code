package another_problems;

public class 求最大公约数 {
    public static int gcd(int m, int n){
        if (n == 0){
            return m;
        }
        return gcd(n, m%n);
    }
    public static int gcd_2(int m, int n){
        int temp;
        while (n != 0){
            temp = n;
            n = m%n;
            m = temp;
        }
        return m;
    }

    public static void main(String[] args) {
        System.out.println(gcd(40,60));
        System.out.println(gcd_2(40,60));
    }
}
