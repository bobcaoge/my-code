package recursion_and_dynamic_programming;

public class 编辑字符串的最小代价 {
    public static int min_cost(int rc, int dc, int ic, String s1, String s2){
        int row = s1.length()+1;
        int column = s2.length()+1;
        int[][] dp = new int[row][column];
        dp[0][0] = 0;
        for (int i=1;i<row;i++){
            dp[i][0] = dp[i-1][0] + ic;
        }
        for (int j=1;j<column;j++){
            dp[0][j] = dp[0][j-1] + ic;
        }
        for (int i=1;i<row;i++){
            for(int j=1;j<column;j++){
                dp[i][j] = Math.min(Math.min(dp[i-1][j] + dc, dp[i][j-1]+ic),s1.charAt(i-1) == s2.charAt(j-1)? dp[i-1][j-1]: dp[i-1][j-1]+ 1);
            }
        }
        return dp[row-1][column-1];
    }
    public static void main(String[] args){
//        System.out.println(min_cost());
    }
}
