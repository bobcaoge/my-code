package string_problems;

import org.omg.Messaging.SYNC_WITH_TRANSPORT;

public class 字符串中数字子串的求和 {
    public static int sum(String s){
        if (s == null || s.length() == 0){
            return 0;
        }
        boolean minus_flag = false;
        int ret = 0;
        s += " ";
        int cur = 0;
        for(int i=0; i<s.length();i++){
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9'){
                cur = cur * 10 + Integer.parseInt(s.substring(i,i+1));
            }
            else{
                ret += minus_flag ? -cur : cur;
                cur = 0;
                if(s.charAt(i) == '-'){
                    if (i>0 && s.charAt(i-1) == '-'){
                        minus_flag = !minus_flag;
                    }else{
                        minus_flag = true;
                    }
                }else{
                    minus_flag = false;
                }
            }
        }
        return ret;
    }
    public static  void main(String[] args){
        System.out.println(sum("-1A1B5-6--100--ABC200"));
//        System.out.println(sum("A1B3-6--100--ABC200"));
    }
}
