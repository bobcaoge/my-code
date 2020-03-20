package string_problems;


public class 括号字符串的有效性和最长有效长度 {
    public static boolean judge(String s){
        if(s == null){
            return false;
        }
        int count1 = 0;
        int count2 = 0;
        for(char c: s.toCharArray()){
            if (c == '('){
                count1 ++;
            }else if(c == ')'){
                if(++count2 > count1){
                    return false;
                }
            }else{
                return false;
            }
        }
        return true;
    }
    public static int length_of_longest_subString(String s){
        if(s == null){
            return 0;
        }
        int max = 0;
        int[] dp = new int[s.length()];
        char[] chas = s.toCharArray();
        int pre = 0;
        for (int i=1;i<s.length();i++){
            if (chas[i] == ')'){
                pre = i - dp[i-1] - 1;
                if(pre >= 0 && chas[pre] == '('){
                    dp[i] = dp[i-1]+2 + pre>0?dp[pre-1]:0;
                }
            }
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
