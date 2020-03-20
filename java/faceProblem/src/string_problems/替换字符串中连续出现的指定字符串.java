package string_problems;

/**
 * 此代码又bug，主函数中的案例不能通过
 */
public class 替换字符串中连续出现的指定字符串 {
    public static String replace(String str, String from, String to){
        if(str == null || from == null || str.equals("") || from.equals("")){
            return str;
        }
        char[] chas = str.toCharArray();
        char[] chaf = from.toCharArray();
        int match = 0;
        for (int i=0;i<chas.length;i++){
            if(chas[i] == chaf[match++]){
                if (match == chaf.length){
                    clear(chas, i, chaf.length);
                    match = 0;
                }
            }else{
                match = 0;
            }
        }
        String res = "";
        String cur = "";
        for (int i=0;i<chas.length;i++){
            if (chas[i] != 0){
                cur = cur + String.valueOf(chas[i]);
            }
            if (chas[i] == 0 && (i == 0 || chas[i-1] != 0)){
                res = res + cur+to;
                cur = "";
            }
        }
        if (!cur.equals("")){
            res = res+cur;
        }
        return res;
    }
    public static void clear(char[] chas, int end, int len){
        while(len-- != 0){
            chas[end--] = 0;
        }
    }
    public static void main(String[] args){
        System.out.println(replace("abcabcadaaaa", "abcad", "1"));
    }
}
