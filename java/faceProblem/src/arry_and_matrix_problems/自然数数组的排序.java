package arry_and_matrix_problems;

public class 自然数数组的排序 {
    public static int[] sort(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums;
        }
        int temp;
        for (int i = 0; i <nums.length ; i++) {
            while(nums[i] != i+1){
                temp = nums[nums[i]-1];
                nums[nums[i]-1] = nums[i];
                nums[i] = temp;
            }
        }
        return nums;
    }
    public static int[] sort1(int[] nums){
        if(nums == null || nums.length <= 1){
            return nums;
        }
        int next;
        int temp;
        for (int i = 0; i <nums.length ; i++) {
            temp = nums[i];
            while(nums[i] != i+1) {
                next = nums[temp-1];
                nums[temp-1] = temp;
                temp = next;

            }
        }
        return nums;
    }


    public static void main(String[] args) {
        int[] result = sort(new int[]{3,2,1,6,4,5});
        for (int num:result) {
            System.out.print(num+" ");
        }
    }
}
