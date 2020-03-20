package recursion_and_dynamic_programming;

public class 汉诺塔 {
    public static void hanoi(int n){
        if (n > 0){
            move(n, "left", "mid", "right");
        }
    }
    public static void move(int n, String from, String mid, String to){
        if (n == 1){
            System.out.println("move from "+from+" to "+to);
        }else{
            move(n-1, from, to, mid);
            move(1, from, mid, to);
            move(n-1, mid, from, to);
        }
    }
    public static int get_state(int[] arr){
        if (arr == null || arr.length == 0){
            return 0;
        }
        return process(arr, arr.length-1, 1,2,3);

    }
    public static int process(int[] arr, int i, int from , int mid, int to){
        if (i == -1){
            return -1;
        }
//        如果当前未移动到目标柱子的最大圆盘不在左柱子或者右柱子上，那就一定不是最优路径
        if(arr[i] != from && arr[i] != to){
            return -1;
        }
//        如果最大圆盘在左柱子上，说明还在执行将i-1个圆盘移动到中间柱子上的步骤
        if (arr[i] == from){
            return process(arr, i-1, from, to, mid);
        }else{
//            如果最大圆盘在右柱子上，说明i-1个圆盘已经移动成功而且最大圆盘也已经移动成功，接着考了i-1个柱子的移动
            int rest = process(arr, i-1, mid, from, to);
            if (rest == -1){
                return -1;
            }
            return 1<<i + rest;
        }

    }
    public static void main(String[] args){
        hanoi(8);
    }


}
