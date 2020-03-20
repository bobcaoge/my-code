import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    HashMap<Integer[], Integer> memo;
    public int get_num(String s, char c){
        int ret = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c){
                ret += 1;
            }
        }
        return ret;
    }

    public int recursion(ArrayList<Integer[]> strs, int start, int m, int n){
        Integer[] key = {start, m, n};
        if (memo.containsKey(key)){
            return memo.get(key);
        }
        int num = 0;
        for (int i = start; i < strs.size() ; i++) {
            int cur_zero_need = strs.get(i)[0];
            int cur_one_need = strs.get(i)[1];
            if (m >= cur_zero_need && n >= cur_one_need) {
                int value = recursion(strs, i + 1, m - cur_zero_need, n - cur_one_need) + 1;
                num = Math.max(num, value);
            }
        }
        memo.put(key, num);
        return num;
    }
    public int findMaxForm(String[] strs, int m, int n) {

        ArrayList<Integer[]> strs2_list = new ArrayList<>();
        int num = 0;
        for (int i = 0; i < strs.length; i++) {
            if (strs[i].equals("0")){
                num ++;
                m --;
            }else if(strs[i].equals("1")){
                num++;
                n--;
            }else{
                strs2_list.add(new Integer[]{get_num(strs[i], '0'), get_num(strs[i], '1')});
            }
        }
        memo = new HashMap<>();
        return num + recursion(strs2_list, 0, m, n);
    }

    public static void main(String[] args) {
        String a = "AAA";
        String b = a;
        a.replace("A", "a");
        System.out.println(a);
        System.out.println(b);

    }
}
