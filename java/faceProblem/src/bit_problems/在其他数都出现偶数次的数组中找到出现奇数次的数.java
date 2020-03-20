package bit_problems;

public class 在其他数都出现偶数次的数组中找到出现奇数次的数 {
    public static int find(int[] nums){
        int ret = 0;
        for (int num:nums) {
            ret ^= num;
        }
        return ret;
    }
    public static int[] find2(int[] nums){
        int buff = find(nums);
        int right_one = buff & (~buff+1);
        int first = 0;
        for(int num:nums){
            if ((num & right_one) != 0){
                first ^= num;
            }
        }
        return new int[]{first, first^buff};
    }

}
