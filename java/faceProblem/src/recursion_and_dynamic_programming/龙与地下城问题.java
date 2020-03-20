package recursion_and_dynamic_programming;

public class 龙与地下城问题 {
    public static int blood(int[][] matrix){
        if (matrix == null){
            return 0;
        }
        int row = matrix.length;
        int column = matrix[0].length;
        int[][] dp = new int[row][column];
        dp[row-1][column-1] = Math.max(1-matrix[row-1][column-1], 1);
        for (int i=row-2;i>=0;i--){
            dp[i][column-1] += Math.max(dp[i+1][column-1]-matrix[i][column-1], 1);
        }
        for (int j=column-2;j>=0;j--){
            dp[row-1][j] = Math.max(dp[row-1][j+1]-matrix[row-1][j], 1);
        }
        for(int i=row-2;i>=0;i--){
            for (int j=column-2;j>=0;j--){
                dp[i][j] = Math.min(Math.max(dp[i][j+1]-matrix[i][j], 1), Math.max(dp[i+1][j]-matrix[i][j], 1));
            }
        }
        return dp[0][0];
    }
    public static void main(String[] args){
        System.out.println(blood(new int[][]{{-2,-3,3},{-5,-10,1},{10,30,-5}}));
    }
}
