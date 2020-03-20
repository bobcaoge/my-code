package string_problems;

public class 添加最少字符使字符串整体都是回文字符串 {
    public static int[][] get_dp(String s){
        if (s == null || s.length() == 0){
            return null;
        }
        int[][] dp = new int[s.length()][s.length()];
        for(int j=1; j<s.length(); j++){
            dp[j-1][j] = s.charAt(j-1) == s.charAt(j) ? 0 : 1;
            for(int i=j-2;i>=0;i--){
                if (s.charAt(i) == s.charAt(j)){
                    dp[i][j] = dp[i+1][j-1];
                }else{
                    dp[i][j] = Math.min(dp[i][j-1], dp[i+1][j])+1;
                }
            }
        }
        return dp;
    }
    public static String get_parl(String s){
        if (s == null || s.length() <=1 ){
            return s;
        }
        int[][] dp = get_dp(s);
        char[] res = new char[s.length()+dp[0][s.length()-1]];
        int l = 0;
        int r = s.length() - 1;
        int resl = 0;
        int resr = res.length-1;
        while (l <= r){
            if (s.charAt(l) == s.charAt(r)){
                res[resl++] = s.charAt(l++);
                res[resr--] = s.charAt(r--);
            }else{
                if (dp[l+1][r] < dp[l][r-1]){
                    res[resl++] = s.charAt(l);
                    res[resr--] = s.charAt(l++);
                }else{
                    res[resl++] = s.charAt(r);
                    res[resr--] = s.charAt(r--);
                }
            }
        }
        return String.valueOf(res);
    }
    public static String get_parl_2(String s, String sub){
        if (s == null || s.length() <= 1){
            return s;
        }
        char[] res = new char[2*s.length()-sub.length()];
        int resl = 0;
        int resr = res.length-1;
        int leftl = 0;
        int leftr = 0;
        int rightl = s.length()-1;
        int rightr = s.length()-1;
        int index_of_sub_l = 0;
        int index_of_sub_r = sub.length()-1;
        char[] chas = s.toCharArray();
        char[] subs = sub.toCharArray();
        while(index_of_sub_l <= index_of_sub_r){
//            System.out.println(String.valueOf(res));
            while (chas[leftr] != subs[index_of_sub_l]){
                leftr ++;
            }
            index_of_sub_l ++;
            while(chas[rightl] != subs[index_of_sub_r]){
                rightl--;
            }
            index_of_sub_r--;
            set(res, chas, resl, resr, leftl, leftr, rightl, rightr);
            resl += leftr - leftl+1+1;
            resr -= rightr - rightl+1+1;
            leftr++;
            leftl = leftr;
            rightl--;
            rightr = rightl;
        }
        return String.valueOf(res);
    }
    public static void set(char[] res, char[] chas, int resl, int resr, int leftl, int leftr, int rightl, int rightr){
        for(int i = 0;i<leftr-leftl+1;i++){
            res[resl++] = chas[leftl];
            res[resr--] = chas[leftl++];
        }
        for(int i = 0;i<rightr-rightl+1;i++){
            res[resl++] = chas[rightr];
            res[resr--] = chas[rightr--];
        }
        res[resl] = chas[leftr];
        res[resr] = chas[rightl];

    }
    public static void main(String[] args){
//        System.out.println(get_parl("abc121cddd"));
        System.out.println(get_parl_2("A1BC22DE1F", "1221"));

    }
}
