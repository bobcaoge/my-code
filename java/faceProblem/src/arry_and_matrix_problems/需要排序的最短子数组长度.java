package arry_and_matrix_problems;

public class 需要排序的最短子数组长度 {
    public static int get(int[] nums){
        if(nums == null || nums.length <= 1){
            return 0;
        }
        int min = nums.length-1;
        int no_min_index = -1;
        for (int i = nums.length-2; i >=0 ; i--) {
            if(nums[i] > min){
                no_min_index = i;
            }else{
                min = nums[i];
            }
        }
        if(no_min_index == -1){
            return 0;
        }
        int max = nums[0];
        int no_max_index = -1;
        for (int i = 1; i <nums.length ; i++) {
            if(nums[i] < max){
                no_max_index = i;
            }else{
                max = nums[i];
            }
        }
        return no_max_index - no_min_index + 1;
    }
}
