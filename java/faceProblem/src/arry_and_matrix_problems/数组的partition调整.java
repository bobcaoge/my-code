package arry_and_matrix_problems;

public class 数组的partition调整 {
    public static int[] partition(int[] nums){
        if(nums == null){
            return nums;
        }
        int u = 0;
        int i = 1;
        while (i<nums.length){
            if(nums[i++] != nums[u]){
                swap(nums, ++u, i-1);
            }
        }
        return nums;
    }
    public static void partition_2(int[] nums){
        if(nums == null || nums.length < 2){
            return;
        }
        int left = -1;
        int right = nums.length;
        int index = 0;
        while (index != right){
            if(nums[index] == 0){
                swap(nums, ++left, index++);
            }else if(nums[index] == 2){
                swap(nums, index++, --right);
            }else{
                index++;
            }
        }
    }
    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
