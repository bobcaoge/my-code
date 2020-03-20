package string_problems;

public class 最小包含子串的长度 {
    public static int get(String s1, String s2){
        if(s2 == null || s1 == null || s2.equals("") || s1.equals("")){
            return 0;
        }
        int left = 0;
        int right = 0;
        int[] map = new int[256];
        int len = Integer.MAX_VALUE;
        int match = s2.length();
        while (right < s1.length()){
            map[s1.charAt(right)]--;
            if(map[s1.charAt(right)] >= 0){
                match --;
            }
            if(match == 0){
                while (map[s1.charAt(left)] < 0){
                    map[s1.charAt(left++)]++;
                }
                match++;
                len = Math.min(right-left+1, len);
                map[s1.charAt(left++)]++;
            }
            right ++;
        }
        return len == Integer.MAX_VALUE ? 0 : len;
    }
}
