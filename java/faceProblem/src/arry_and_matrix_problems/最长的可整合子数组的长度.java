package arry_and_matrix_problems;

import java.util.HashSet;

public class 最长的可整合子数组的长度 {
    public static int find(int[] nums){
        if(nums == null || nums.length == 0){
            return 0;
        }
        int len = 0;
        int max;
        int min;
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i <nums.length ; i++) {

            max = Integer.MIN_VALUE;
            min = Integer.MAX_VALUE;
            for (int j = i; j <nums.length ; j++) {
                if (set.contains(nums[j])){
                    break;
                }
                set.add(nums[j]);
                min = Math.min(min, nums[j]);
                max = Math.max(max, nums[j]);
                if(max-min == j-i){
                    len = Math.max(len, j-i);
                }
            }
            set.clear();
        }
        return len;
    }
}
