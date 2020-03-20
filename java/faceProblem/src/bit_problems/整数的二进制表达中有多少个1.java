package bit_problems;

public class 整数的二进制表达中有多少个1 {
    public static int count(int a){
        int res = 0;
        while (a != 0){
            res += a & 1;
            a >>>=1;
        }
        return res;
    }
    public static int count2(int a){
        int res = 0;
        while(a != 0){
            a &= (a-1);
            res ++;
        }
        return res;
    }
}
