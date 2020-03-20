package recursion_and_dynamic_programming;

import org.omg.Messaging.SYNC_WITH_TRANSPORT;

public class 两个字符串的最长子串 {
    public static int[][] getdp(String a, String b){
        char[] s1 = a.toCharArray();
        char[] s2 = b.toCharArray();
        int[][] dp  = new int[s1.length][s2.length];
        dp[0][0] = s1[0]==s2[0]?1:0;
        for(int i=1;i<s1.length;i++){
            dp[i][0] = s1[i] == s2[0]? 1:0;
        }
        for (int j=1;j<s2.length;j++){
            dp[0][j] = s1[0] == s2[j] ? 1 : 0;
        }
        for(int i=1;i<s1.length;i++){
            for(int j=1;j<s2.length;j++){
                if(s1[i] == s2[j]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
            }
        }
        return dp;
    }
    public static String get_longest_common_subString_1(String s1, String s2){
        int[][] dp = getdp(s1, s2);
        String ret = "";
        String cur = "";
        int row = -1;
        int column = -1;
        int max = -1;
        for (int i=0;i<s1.length();i++){
            for(int j=0;j<s2.length();j++){
                 if (dp[i][j] > max){
                     max = dp[i][j];
                     row = i;
                     column = j;
                 }
            }
        }
        ret = s1.substring(row+1-dp[row][column], row+1);
        return ret;
    }
    public static String get_longest_common_subString(String s1, String s2){
        int row = 0;
        int max = -1;
        int pos = -1;
        int column = s2.length()-1;
        while (row < s1.length()){
            int len = 0;
            int i = row;
            int j= column;
            while (j< s2.length() && i < s1.length()){
                if (s1.charAt(i++) == s2.charAt(j++)){
                    len ++;
                }else{
                    len = 0;
                }
                if (len>max){
                    max = len;
                    pos = i;
                }
            }
            if (column > 0){
                column -- ;
            }else{
                row ++;
            }
        }
        return s1.substring(pos-max, pos);
    }
    public static void main(String[] args){
        int[][] dp = getdp("12345", "1121365");
        for(int i = 0;i< dp.length; i++){
            for(int j=0;j<dp[0].length;j++){
                System.out.print(dp[i][j]+" "+"("+i+" , "+j+")");
            }
            System.out.println();
        }
        System.out.println(get_longest_common_subString_1("1AB2345CD", "12345EF"));
        System.out.println(get_longest_common_subString("1A2345CD", "12345EF"));
    }
}
