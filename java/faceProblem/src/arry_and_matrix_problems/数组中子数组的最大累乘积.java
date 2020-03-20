package arry_and_matrix_problems;

public class 数组中子数组的最大累乘积 {
    public static int max_sum(int[] nums){
        if(nums == null || nums.length ==0){
            return 0;
        }
        int max = nums[0];
        int min = nums[0];
        int ret = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int cur_max = Math.max(Math.max(max*nums[i], min*nums[i]), nums[i]);
            int cur_min = Math.min(Math.min(max*nums[i], min*nums[i]), nums[i]);
            max = cur_max;
            min = cur_min;
            ret = Math.max(ret, max);
        }
        return max;
    }
}
