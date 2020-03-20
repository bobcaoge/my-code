package string_problems;

public class 在有序但含有空的数组中查找字符串 {
    public static int find(String[] strs, String target){
        if(strs == null || target == null || strs.length == 0){
            return -1;
        }
        int left = 0;
        int right = strs.length-1;
        int mid = (left + right)/2;
        int res = -1;
        while (left <= right){
            if (strs[mid].equals(target)){
                res = -1;
                right = mid - 1;
            }else{
                int i = mid;
                for(; i >= left; i--){
                    if (strs[i] == null){
                        continue;
                    }
                    if (0 < strs[i].compareTo(target)){
                        right = i - 1;
                    }else if (0 == strs[i].compareTo(target)){
                        res = i;
                        right = i - 1;
                    }else{
                        left = mid + 1;
                    }
                    break;
                }
                if (i == left){
                    left  = mid + 1;
                }
            }
            mid = (left + right)/2;
        }
        return res;
    }

}
