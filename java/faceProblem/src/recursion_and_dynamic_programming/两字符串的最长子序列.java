package recursion_and_dynamic_programming;

public class 两字符串的最长子序列 {
    public static int[][] getdp(String s1, String s2){
        int[][] dp = new int[s1.length()][s2.length()];
        // 计算第一列
        dp[0][0] = s1.charAt(0) == s2.charAt(0)?1:0;

        for (int i=1;i<s1.length();i++){
            dp[i][0] = Math.max(dp[i-1][0], s2.charAt(0) == s1.charAt(i)?1:0);
        }
        for (int j=1;j<s2.length();j++){
            dp[0][j] = Math.max(dp[0][j-1], s2.charAt(j) == s1.charAt(0)?1:0);
        }
        for (int i = 1;i<s1.length();i++){
            for (int j=1;j<s2.length();j++){
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                if (s1.charAt(i) == s2.charAt(j)){
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1]+1);
                }
            }
        }
        return dp;
    }
    public static String get_longest_common_string(String s1, String s2){
        int[][] dp = getdp(s1, s2);
        int row = s1.length()-1;
        int column = s2.length()-1;
        char[] ret = new char[dp[row][column]];
        int pos = ret.length-1;
        while (pos >= 0){
            if (row > 0 && dp[row][column] == dp[row-1][column]){
                row--;
            }else if(column>0 && dp[row][column] == dp[row][column-1]){
                column--;
            }else{
                ret[pos--] = s1.charAt(row);
                row--;
                column--;
            }
        }
        return String.valueOf(ret);
    }
    public static void main(String[] args){
        String res = get_longest_common_string("1A2C3D4B56", "B1D23CA45B6A");
        System.out.println(res);
    }
}
