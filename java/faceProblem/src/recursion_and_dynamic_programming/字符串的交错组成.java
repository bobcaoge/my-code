package recursion_and_dynamic_programming;

public class 字符串的交错组成 {
    public static boolean judge(String s1, String s2, String aim){
        if (s1 == null || s2 == null || aim == null || s1.length()+s2.length()!= aim.length()){
            return false;
        }

        boolean[][] dp = new boolean[s1.length()+1][s2.length()+1];
        dp[0][0] = true;
        for (int i=1; i<s1.length()+1; i++){
            if(s1.charAt(i-1) != aim.charAt(i-1)){
                break;
            }
            dp[i][0] = true;
        }
        for(int j=1; j<s2.length()+1;j++){
            if ( s2.charAt(j-1) != aim.charAt(j-1)){
                break;
            }
            dp[0][j] = true;
        }
        for(int i=1; i<s1.length()+1;i++){
            for(int j=1;j<s2.length()+1;j++){
                if (dp[i-1][j] && aim.charAt(i+j-1) == s1.charAt(i-1) || dp[i][j-1] && aim.charAt(i+j-1) == s2.charAt(j-1))
                dp[i][j] = true ;
            }
        }
        return dp[s1.length()][s2.length()];

    }
}
