package arry_and_matrix_problems;

public class 未排序数组中累加和小千或等于给定值的最长子数组长度 {
    public static int find(int[] nums, int target){
        //生成numarr 即0-i的累加和数组
        int[] num_arr = new int[nums.length];
        int last = 0;
        for (int i = 0; i < nums.length; i++) {
            last += nums[i];
            num_arr[i] = last;
        }
        //生成helparr 即累加和num最早出现的数组
        int[] help_arr;
        help_arr = num_arr.clone();
        for (int i = 1; i < help_arr.length; i++) {
            help_arr[i] = Math.max(help_arr[i], help_arr[i-1]);
        }
        int ret = 0;
        for (int i = 0; i < num_arr.length; i++) {
            if(num_arr[i] <= target){
                ret = i+1;
            }else{
                int index = search(help_arr, num_arr[i]-target, i);
                if (index != -1){
                    ret = Math.max(ret, i-index);
                }
            }
        }
        return ret;
    }

    public static int search(int[] nums, int target, int end){
        if(nums == null || nums.length == 0){
            return -1;
        }
        int start = 0;
        int mid = (start + end)/2;
        int ret = -1;
        while (start <= end){
            if(nums[mid] >= target){
                ret = mid;
                end = mid-1;
            }else{
                start = mid+1;
            }
            mid = (start + end)/2;
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(find(new int[]{3, -2, -4, 0, 6}, 2));
    }
}
