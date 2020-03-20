package arry_and_matrix_problems;

public class 不包含本位置值的累乘数组 {
    public static int[] manger(int[] nums){
        int[] right_to_left = new int[nums.length];
        int last = 1;
        for (int i = nums.length-1; i >=0 ; i--) {
            last *= nums[i];
            right_to_left[i] = last;
        }
        last = 1;
        for (int i = 0; i < nums.length; i++) {
            right_to_left[i] = i+1 < nums.length ? last*right_to_left[i+1] : last;
            last *= nums[i];
            nums[i] = last;
        }
        return right_to_left;
    }
    public static int[] manger1(int[] nums){
        int all = 1;
        int index_of_zero = -1;
        boolean have_recorded = false;
        int[] ret = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == 0 && (!have_recorded)){
                have_recorded = true;
                index_of_zero = i;
            }else {
                all *= nums[i];
            }
        }
        if(index_of_zero >= 0){
            ret[index_of_zero] = all;
            for (int i = 0; i <nums.length && i!=index_of_zero ; i++) {
                ret[i] = 0;
            }
        }else{
            for (int i = 0; i <nums.length ; i++) {
                ret[i] = all/nums[i];
            }
        }
        return ret;
    }

}
