package arry_and_matrix_problems;

public class 在数组中找到一个局部最小的位置 {
    public static int find(int[] nums){
        if(nums == null || nums.length == 0){
            return -1;
        }
        if(nums.length <= 2){
            return 0;
        }
        if(nums[0] < nums[1]){
            return 0;
        }
        if(nums[nums.length-1] < nums[nums.length-2]){
            return nums.length-1;
        }
        int left = 1;
        int right = nums.length-2;
        int mid = (left + right)/2;
        while(left != right){
            if(nums[mid] > nums[mid-1]){
                right = mid-1;
            }else if(nums[mid] < nums[mid-1]){
                left = mid + 1;
            }else{
                return mid;
            }
            mid = (left + right)/2;
        }
        return -1;
    }
}
