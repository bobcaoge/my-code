package bit_problems;

public class 只用位运算不用算术运算实现整数的加减乘除运算 {
    public static int add(int a, int b){
        int carry;
        while(b != 0){
            carry = (a&b)<<1;
            a = a^b;
            b = carry;
        }
        return a;
    }
    public static int minus(int a, int b){
        return add(a ,add(~b, 1));
    }

    public static int multiple(int a, int b){
        int res = 0;
        while(b != 0){
            if((b&1) != 0){
                res = add(res, a);
            }
            a <<= 1;
            b >>>= 1;
        }
        return res;
    }

    public static int div(int a, int b){
        int x = a < 0 ? minus(0, a) : a;
        int y = b < 0 ? minus(0, b) : b;
        int res = 0;
        for (int i = 31; i > -1 ; i=minus(i, 1)) {
            if((x >> i) >= y){
                res |= 1<<i;
                x = minus(x, y<<i);
            }
        }
        return (a < 0) ^ (b < 0) ? minus(0, res) : res;
    }
    public static int divide(int a, int b){
        if (a == 0){
            return 0;
        }else if(a == Integer.MIN_VALUE && b == Integer.MIN_VALUE){
            return 1;
        }else if(a == Integer.MIN_VALUE){
            int res = div(add(a, 1), b);
            return add(res, div(minus(a, multiple(res, b)), b));
        }else if(b == Integer.MIN_VALUE){
            return 0;
        }else{
            return div(a, b);
        }

    }
    public static void main(String[] args) {
        System.out.println(add(133,244));
        System.out.println(minus(133,244));
        System.out.println(multiple(101,200));
        System.out.println(divide(200,200));
    }
}
