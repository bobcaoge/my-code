package string_problems;

public class 两字符串是否互为旋转词 {
    public static boolean judge(String s1, String s2){
        if(s1 == null || s2 == null || s1.length() != s2.length()){
            return false;
        }
        return (s1+s1).contains(s2);
    }
}
