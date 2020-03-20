package arry_and_matrix_problems;

import java.util.HashMap;

public class 未排序数组中累加和为给定值的最长子数组系列问题 {
    public static int find(int[] nums, int k){
        if(nums == null || nums.length == 0){
            return 0;
        }
        int len = 0;
        int sum = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for (int i = 0; i <nums.length ; i++) {
            sum += nums[i];
            if(map.keySet().contains(sum-k)){
                len = Math.max(len, i - map.get(sum-k));
            }
            if(!map.keySet().contains(sum)){
                map.put(sum, i);
            }
        }
        return len;
    }
}
