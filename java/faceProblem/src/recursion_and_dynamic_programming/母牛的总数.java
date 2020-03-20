package recursion_and_dynamic_programming;

public class 母牛的总数 {
    public static int get(int n){
        /**
         * n represents the year
         */
        if (n < 1){
            return 0;
        }
        if (n == 1 || n== 2 || n== 3){
            return n;
        }
        return get(n-1) + get(n-3);
    }
    public static int get_2(int n){
        if (n < 1){
            return 0;
        }
        if (n == 1 || n== 2 || n== 3){
            return n;
        }
        int[] nums = new int[n+1];
        nums[0] = 0;
        nums[1] = 1;
        nums[2] = 2;
        nums[3] = 3;
        for(int i=4; i<=n;i++){
            nums[i] = nums[i-1]+nums[i-3];
        }
        return nums[n];
    }
}
