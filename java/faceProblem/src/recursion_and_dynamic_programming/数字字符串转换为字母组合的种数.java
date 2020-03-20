package recursion_and_dynamic_programming;

public class 数字字符串转换为字母组合的种数 {
    public static int translate(String s){
        int old_used = 0;
        int old_not_used = 0;
        for(int i=0; i<s.length(); i++){
            if (i==0){
                if (s.charAt(i) != '0'){
                    old_not_used = 1;
                    old_used = 1;
                }
            }else{
                int cur_used = 0;
                if ( s.charAt(i) != '0'){
                    cur_used += old_used;
                }
                if( s.charAt(i-1) == '1' ||
                 s.charAt(i-1) == '2' && s.charAt(i) <= '6'){
                    cur_used += old_not_used;
                }
                old_not_used = old_used;
                old_used = cur_used;
            }
            if (old_not_used == 0 && old_used == 0){
                return 0;
            }
        }
        return old_used;
    }
    public static void main(String[] args){
        System.out.println(translate("12"));
        System.out.println(translate("1111"));
        System.out.println(translate("0111"));
    }
}
