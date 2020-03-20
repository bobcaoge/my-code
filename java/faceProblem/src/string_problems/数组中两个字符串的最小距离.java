package string_problems;

import java.util.HashMap;
import java.util.Map;

public class 数组中两个字符串的最小距离 {
    public static int min_distance(String[] s, String s1, String s2){
        if(s1 == null || s2 == null||s == null || s.length == 0){
            return -1;
        }
        if (s1.equals(s2)){
            return 1;
        }
        int min = Integer.MAX_VALUE;
        int last1 = -1;
        int last2 = -1;
        for(int i=0;i<s.length;i++){
            if(s1.equals(s[i])){
                min = Math.min(min, last2!= -1?i-last2:min);
                last1 = i;
            }
            if(s2.equals(s[i])){
                min = Math.min(min, last1!= -1?i-last1:min);
                last2 = i;
            }
        }
        return min!=Integer.MAX_VALUE?min:-1;
    }
}
class Record{
    HashMap<String, HashMap<String, Integer>> record;
    Record(String[] strs){
        record = new HashMap<>();
        if (strs == null || strs.length == 0){
            return;
        }
        HashMap<String, Integer> index_map = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            update(index_map, strs[i], i);
            index_map.put(strs[i], i);
        }
    }
    public void update(HashMap<String, Integer> index_map, String s, int index){
        if(!record.containsKey(s)){
            record.put(s, new HashMap<>());
        }
        HashMap<String, Integer> s_map = record.get(s);
        for(Map.Entry<String, Integer> last_entry: index_map.entrySet()){
            String key = last_entry.getKey();
            int i = last_entry.getValue();
            if(!key.equals(s)){
                HashMap<String, Integer> last_map = record.get(key);
                int cur_min = index-i;
                if (last_map.containsKey(s)){
                    cur_min = Math.min(last_map.get(s), cur_min);
                    last_map.put(s, cur_min);
                    s_map.put(key, cur_min);
                }else{
                    last_map.put(s, cur_min);
                    s_map.put(key, cur_min);
                }
            }
        }
    }
    public  int min_distance(String[] s, String s1, String s2) {
        if (s1 == null || s2 == null || s == null || s.length == 0) {
            return -1;
        }
        if (s1.equals(s2)) {
            return 1;
        }
        if (record.get(s1).containsKey(s2) && record.get(s2).containsKey(s1)){
            return record.get(s1).get(s2);
        }
        return -1;
    }
}
