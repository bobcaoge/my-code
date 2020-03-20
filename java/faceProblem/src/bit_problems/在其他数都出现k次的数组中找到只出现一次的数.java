package bit_problems;

public class 在其他数都出现k次的数组中找到只出现一次的数 {
    public static int once_num(int[] nums, int k){
        int[] k_num = new int[32];
        for (int num:nums) {
            set_k_num(k_num, num, k);
        }
        return k_to_ten_num(k_num, k);
    }
    public static void set_k_num(int[] nums, int num, int k){
        int[] to_plus = to_k_num(num, k);
        for (int i = 0; i <nums.length; i++) {
            nums[i] = (nums[i] + to_plus[i]) % k;
        }
    }
    public static int[] to_k_num(int value, int k){
        int[] nums = new int[32];
        int i = 0;
        while(value != 0){
            nums[i++] = value % k;
            value /= k;
        }
        return nums;
    }
    public static int k_to_ten_num(int[] nums, int k){
        int ret = 0;
        int carry = 1;
        for (int num: nums) {
            ret += num*carry;
            carry *= k;
        }
        return ret;
    }
}
