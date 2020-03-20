package recursion_and_dynamic_programming;

public class 跳跃游戏 {
    public static int jump(int[] arr){
        if (arr == null || arr.length == 0){
            return 0;
        }
        return recursion(arr, 0, 0);

    }
    public static int recursion(int[] arr, int pos, int path){
        if (arr.length == pos+1){
            return path;
        }
        int ret = Integer.MAX_VALUE;
        for(int i=pos; i<pos+arr[i];i++){
            ret = Math.min(ret, recursion(arr, i, path+1));
        }
        return ret;
    }
    public static int jump_2(int[] arr){
        if (arr == null || arr.length == 0) {
            return 0;
        }
        int[] dp = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            dp[i] = Integer.MAX_VALUE;
        }
        dp[arr.length-1] = 0;
        for (int i=arr.length-2;i>=0;i--){
//            for(int x: dp){
//                System.out.print(x+" ");
//            }
//            System.out.println();
            for(int j=i+1; j<=i+arr[i] && j < dp.length;j++){
//                System.out.println(j);
                if (dp[j] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
            for(int x: dp){
                System.out.print(x+" ");
            }
            System.out.println();
        }
        return dp[0];
    }
    public static int recursion_2(int[] arr, int pos, int depth){
        if (pos == arr.length){
            return depth;
        }
        int ret = Integer.MAX_VALUE;
        for(int i=pos+1;i<=pos+arr[i] && i<arr.length; i++){
            ret = Math.min(ret, recursion_2(arr, i, depth+1));
        }
        return ret;
    }
    public static int jump_3(int[] arr){
        if(arr == null || arr.length ==0){
            return 0;
        }
        int jump = 0;
        int cur = 0;
        int next = 0;
        for(int i=0;i<arr.length;i++){
            if (cur < i){
                jump++;
                cur = next;
            }
            next = Math.max(next, i+arr[i]);
        }
        return jump;
    }
    public static void main(String[] args){
        System.out.println(jump_3(new int[]{2,3,0,1,4}));
    }
}
