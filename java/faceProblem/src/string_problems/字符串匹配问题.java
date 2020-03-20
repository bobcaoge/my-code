package string_problems;

public class 字符串匹配问题 {
    public static boolean judge(String a, String b){
        if(a == null || b == null){
            return false;
        }
        char[] chara = a.toCharArray();
        char[] charb = b.toCharArray();
        return process(chara, charb, 0, 0);

    }
    public static boolean process(char[] a, char[] b, int ai, int bi){
        if(bi == b.length){
            return ai==a.length;
        }
        if(bi+1 == b.length || b[bi+1]!='*'){
            return ai != a.length && (a[ai] == b[bi] || b[bi] =='.')
                    && process(a, b, ai+1, bi+1);
        }
        while(ai != a.length && (a[ai] == b[bi] || b[bi] == '.')){
            if(process(a, b, ai, bi+2)){
                return true;
            }
            ai++;
        }
        return process(a, b, ai, bi+2);
    }
    public static boolean dp_judge(String a, String b){
        if(a == null || b == null ){
            return false;
        }
        char[] chara = a.toCharArray();
        char[] charb = b.toCharArray();
        boolean[][] dp = init_dp_map(chara,charb);
        for(int i=a.length()-1;i>=0;i--){
            for(int j=b.length()-2;j>=0;j--){
                if(charb[j+1] != '*'){
                    dp[i][j] = i != a.length() && (chara[i] == charb[j]|| charb[j]=='.') && dp[i+1][j+1];
                }else{
                    int si = i;
                    while(si != a.length() && (chara[si] == charb[j] || charb[j] == '.')){
                        if (dp[si][j+2]){
                            dp[si][j] = true;
                            break;
                        }
                        si++;
                    }
                    if(!dp[i][j]){
                        dp[i][j] = dp[si][j+2];
                    }
                }
            }
        }
        return dp[0][0];
    }
    public static boolean[][] init_dp_map(char[] a, char[] b){
        boolean [][] dp = new boolean[a.length+1][b.length+1];
        dp[a.length][b.length] = true;
        // calculate value of  dp in last row
        for(int j=b.length-2; j>=0; j-=2){
            if(b[j+1] == '*'){
                dp[a.length][j] = true;
            }else{
                break;
            }
        }
        // c
        if(a.length > 0 && b.length > 0){
            if (a[a.length-1] == b[b.length-1] || b[b.length-1] == '.'){
                dp[a.length-1][b.length-1] = true;
            }
        }
        return dp;
    }
    public static void main(String[] args){
        System.out.println(dp_judge("", "a*a*"));
    }
}
