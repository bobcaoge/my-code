package recursion_and_dynamic_programming;

import java.util.HashMap;

public class 数组中的最长连续序列 {
    public static int longest_consecutive_subsequense(int[] arr){
        int max = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<arr.length;i++){
            if (map.containsKey(arr[i])){
                continue;
            }
            map.put(arr[i], 1);
            if (map.containsKey(arr[i]-1)) {
                int lenA = map.get(arr[i] - 1);
                if (lenA != 0) {
                    map.put(arr[i], lenA + 1);
                    map.put(arr[i] - lenA, lenA + 1);
                    max = Math.max(max, lenA + 1);
                }
            }
            if (map.containsKey(arr[i]+1)) {
                int lenB = map.get(arr[i] + 1);
                if (lenB != 0) {
                    int lenA = map.get(arr[i]);
                    map.put(arr[i] + lenB, lenA + lenB);
                    map.put(arr[i] - lenA + 1, lenA + lenB);
                    max = Math.max(max, lenB + lenA);
                }
            }
        }
        return max;
    }
    public static void main(String[] args){
        System.out.println(longest_consecutive_subsequense(new int[]{1,100,2,200,3,6,5,4, 5,300}));
    }
}
