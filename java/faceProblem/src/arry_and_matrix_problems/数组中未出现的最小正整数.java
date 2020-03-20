package arry_and_matrix_problems;

public class 数组中未出现的最小正整数 {
    public static int find(int[] nums){
        if(nums == null || nums.length == 0){
            return 1;
        }
        int l = 0;
        int r = nums.length;
        while (l<r){
            if(nums[l] == l+1){
                l++;
            }else if(nums[l] <= 1 || nums[l] > r || nums[nums[l]-1] == nums[l]){
                nums[l] = nums[--r];
            }else{
                swap(nums, l, nums[l]-1);
            }
        }
        return l+1;
    }
    public static void swap(int[] nums, int i, int j){
        int temp  = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
