package string_problems;

import java.util.Arrays;
import java.util.Comparator;

class Mycomparator implements Comparator<String> {
    public int compare(String a, String b){
        return (a+b).compareTo(b+a);
    }
}
public class 拼接所有字符串产生字典顺序最小的大写字符串 {
    public static String get_string(String[] strs){
        if (strs == null){
            return "";
        }
        Arrays.sort(strs, new Mycomparator());
        StringBuffer sb = new StringBuffer();
        for(String s:strs){
            sb.append(s);
        }
        return sb.toString();
    }
    public static void main(String[] args){
        System.out.println(get_string(new String[]{"a", "b", "c"}));
    }
}
