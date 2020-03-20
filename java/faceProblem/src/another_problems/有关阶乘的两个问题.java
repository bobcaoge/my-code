package another_problems;

public class 有关阶乘的两个问题 {
    public static int zeroNum1(int m){
        if (m<0){
            return 0;
        }
        int res = 0;
        int num;
        for (int i = 1; i <= m; i++) {
            num = i;
            while(num % 5 == 0){
                res++;
                num /= 5;
            }
        }
        return res;
    }
    public static int zeroNum2(int m){
        if (m<0){
            return 0;
        }
        int res = 0;
        while (m != 0){
            res += m/5;
            m /= 5;
        }
        return res;
    }
    public static int rightOnes(int m){
        if (m<1){
            return -1;
        }
        int ones = 0;
        while (m!=0){
            m>>>=1;
            ones += m;
        }
        return ones;
    }
}
