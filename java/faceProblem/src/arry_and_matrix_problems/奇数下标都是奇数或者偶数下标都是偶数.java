package arry_and_matrix_problems;

public class 奇数下标都是奇数或者偶数下标都是偶数 {
    public static int[] set(int[] nums){
        if(nums == null || nums.length < 2){
            return nums;
        }
        int even = 0;
        int odd = 1;
        int end = nums.length-1;
        while(even<nums.length && odd < nums.length){
            if(nums[end] % 2 == 0){
                swap(nums, even, end);
                even += 2;
            }else{
                swap(nums, odd, end);
                odd += 2;
            }
        }
        return nums;
    }
    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = set(new int[]{1,8,3,2,4,6});
        for (int num:nums) {
            System.out.print(num+" ");
        }
    }
}
