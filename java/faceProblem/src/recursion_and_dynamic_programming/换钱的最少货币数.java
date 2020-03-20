package recursion_and_dynamic_programming;

import java.util.HashSet;

public class 换钱的最少货币数 {
    public static int coinChange(int[] arr, int target){
        if (target == 0){
            return 0;
        }
        int[] nums = new int[target+1];
        for(int i=0;i<target+1;i++){

            nums[i] = Integer.MAX_VALUE;
        }
        nums[0] = 0;
        HashSet<Integer> coins = new HashSet<Integer>();
        for(int coin:arr){
            coins.add(coin);
        }
        for (int i=0;i<target+1;i++){

            if (coins.contains(i)){
                nums[i] = 1;
                continue;
            }
            for (int coin : arr){
                if (i-coin >= 0 && nums[i-coin] != Integer.MAX_VALUE){
                    nums[i] = Math.min(nums[i-coin]+1, nums[i]);
                }
            }
        }
        for (int i: nums) {
            System.out.print(i+" ");

        }
        return nums[target] == Integer.MAX_VALUE ? -1 : nums[target];
    }
    public static void main(String[] args){
        int[] arr= {1,2,5};
        int target = 11;
        int result = coinChange(arr, target);
        System.out.println();
        System.out.print(result);

    }
}
