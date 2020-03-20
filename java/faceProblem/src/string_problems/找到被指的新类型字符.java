package string_problems;

public class 找到被指的新类型字符 {
    public static String pointNewString(String s, int k){
        if(s == null || s.length()==0 || k<0){
            return s;
        }
        int num = 0;
        for(int i=k-1;s.charAt(i)>='A' && s.charAt(i)<='Z';i--){
            num++;
        }
        if (num %2 == 1){
            return s.substring(k-1,k+1);
        }else{
            if (s.charAt(k)<='z' && s.charAt(k)>='a'){
                return s.substring(k,k+1);
            }else{
                return s.substring(k,k+2);
            }
        }
    }
}
