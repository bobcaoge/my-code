package string_problems;

public class 回文最少分割数 {
    public static int get(String s){
        if (s == null || s.length() <= 1){
            return 0;
        }
        int[] dp = new int[s.length()+1];
        boolean[][] p = new boolean[s.length()][s.length()];
        dp[s.length()] = -1;
        for (int i=s.length()-1;i>=0;i--){
            dp[i] = Integer.MAX_VALUE;
            for(int j=i;j<s.length();j++){
                if(s.charAt(i) == s.charAt(j) && (j-i < 2 || p[i+1][j-1])){
                    dp[i] = Math.min(dp[i], dp[j+1]+1);
                    p[i][j] = true;
                }
            }
        }
        return dp[0];
    }
}
