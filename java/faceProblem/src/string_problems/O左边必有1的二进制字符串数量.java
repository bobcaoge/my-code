package string_problems;

public class O左边必有1的二进制字符串数量 {
    public static int get_nums(int n){
        if (n <= 0){
            return 0;
        }
        int old_zero = 0;
        int old_one = 1;
        int cur_zero;
        int cur_one;
        for(int i=1;i<n;i++){
            cur_one = old_one+old_zero;
            cur_zero = old_one;
            old_one = cur_one;
            old_zero = cur_zero;
        }
        return old_one+old_zero;
    }
    public static void main(String[] args){
        for(int i=1;i<=8;i++){
            System.out.println(get_nums(i));
        }
    }
}
