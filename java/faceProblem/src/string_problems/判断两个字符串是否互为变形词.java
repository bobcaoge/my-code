package string_problems;

public class 判断两个字符串是否互为变形词 {
    public static boolean judge(String s1, String s2){
        if (s1 == null || s2 == null || s1.length() != s2.length()){
            return false;
        }
        int[] map = new int[256];
        for (int i=0;i<s1.length();i++){
            map[s1.charAt(i)] ++;
        }
        for (int i=0;i<s2.length();i++){
            if (map[s2.charAt(i)]-- == 0){
                return false;
            }
        }
        return true;
    }
}
