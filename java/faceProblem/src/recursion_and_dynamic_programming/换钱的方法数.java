package recursion_and_dynamic_programming;

import java.util.HashSet;

public class 换钱的方法数 {
    public static int buffer(int[] coins,int index, int target){
        if (index == coins.length){
            if (target == 0){
                return 1;
            }
            return 0;
        }
        int ret = 0;
        for (int i =0; i*coins[index] <= target;i++){
            ret += buffer(coins, index+1, target-i*coins[index]);
        }
        return ret;
    }
    public static int buffer1(int[] coins,int index, int target, int[][] map){
        int ret = 0;
        if (index == coins.length){
            if (target == 0){
                return 1;
            }
        }else {
            for (int i = 0; i * coins[index] <= target; i++) {
                int mapvalue = map[index + 1][target - coins[index] * i];
                if (mapvalue == 0) {
                    ret += buffer1(coins, index + 1, target - i * coins[index], map);
                } else {
                    ret += mapvalue == -1 ? 0 : mapvalue;
                }
            }
            map[index][target] = ret;
        }
        return ret;
    }
    public static int changCoins(int[] coins, int target){
        int[][] map = new int[coins.length+1][target+1];
        return buffer1(coins, 0, target, map);
//        return buffer(coins, 0, target);
    }
    public static int changeCoins(int[] coins, int target){

        if (target < 0){
            return 0;
        }
        int[][] dp = new int[coins.length][target+1];
        for(int i=0;i<coins.length;i++){
            dp[i][0] = 1;
        }
        for(int i=0;i*coins[0]<=target;i++){
            dp[0][i*coins[0]] = 1;
        }
        for (int i=1;i<coins.length;i++){
            for(int j=1;j<target+1;j++){
                for(int k=0;k*coins[i]<=j;k++){
                    dp[i][j] += dp[i-1][j-k*coins[i]];
                }
            }
        }

        return dp[coins.length-1][target];
    }
    public static void main(String[] args){
//        System.out.print(changeCoins(new int[]{1,2,5}, 20));
        System.out.print(changeCoins(new int[]{}, 0));
    }
}
