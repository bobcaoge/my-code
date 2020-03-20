package recursion_and_dynamic_programming;
import java.util.ArrayList;

public class 表达式得到期望结果的组成种数 {
    public static ArrayList<Boolean> get_all(String s){
        ArrayList<Boolean> results = new ArrayList<>();
        if (s.length()==1){
            results.add(s.equals("1"));
            return results;
        }
        for (int i=0;i<s.length();i++){
            if (s.charAt(i) == '|' || s.charAt(i) == '&' || s.charAt(i) == '^'){
                ArrayList<Boolean> left = get_all(s.substring(0, i));
                ArrayList<Boolean> right = get_all(s.substring(i+1));
                for (boolean res1: left){
                    for(boolean res2: right){
                        if (s.charAt(i) == '|'){
                            results.add(res1 | res2);
                        }else if(s.charAt(i) == '&'){
                            results.add(res1 & res2);
                        }else{
                            results.add(res1^res2);
                        }

                    }
                }
            }
        }
        return results;
    }
    public static int get(String s, boolean result){
        ArrayList<Boolean> results = get_all(s);
        int ret = 0;
        for(boolean res: results){
            ret += res==result ? 1 : 0;
        }
        return ret;
    }
    public static int get_2(String s, boolean result){
        int[][] t = new int[s.length()][s.length()];
        int[][] f = new int[s.length()][s.length()];
        t[0][0] = s.charAt(0) == '0' ? 0 : 1;
        f[0][0] = s.charAt(0) == '0' ? 1 : 0;
        for (int i = 2; i<s.length(); i += 2){
            t[i][i] = s.charAt(i) == '0' ? 0: 1;
            f[i][i] = s.charAt(i) == '0' ? 1 : 0;
            for(int j=i-2; j>=0; j-=2){
                for(int k=j; k < i; k+= 2){
                    break;
                }
            }
        }
        if (!result){
            return f[s.length()-1][s.length()-1];
        }else{
            return t[s.length()-1][s.length()-1];
        }
    }
    public static void main(String[] args){
        System.out.println(get("1^0|0|1", false));
    }
}
