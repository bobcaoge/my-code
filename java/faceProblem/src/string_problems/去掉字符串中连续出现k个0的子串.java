package string_problems;

public class 去掉字符串中连续出现k个0的子串 {
    public static String remove_k_zeros(String s, int k){
        if (s == null || s.length() < k || k <= 0){
            return s;
        }
        String ret = "";
        String cur = "";
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == '0'){
                cur = cur + "0";
                if (cur.length() == k){
                    cur = "";
                }
            }else{
                ret = ret + cur + s.substring(i,i+1);
                cur = "";
            }
        }
        ret += cur;
        return ret;
    }
    public static void main(String[] args){
        System.out.println(remove_k_zeros("A000B00", 3));
    }
}
