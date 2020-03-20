package string_problems;

public class 找到字符串的最长无重复字符子串 {
    public static int get(String s){
        if(s == null || s.length() == 0){
            return 0;
        }
        int[] map = new int[256];
        for(int i=0;i<256;i++){
            map[i] = -1;
        }
        int pre = -1;
        int cur = 0;
        int len = 0;
        for(int i=0;i<s.length();i++){
            pre = Math.max(pre, map[s.charAt(i)]);
            cur = i - pre;
            len = Math.max(len, cur);
            map[s.charAt(i)] = i;
        }
        return len;
    }
}
