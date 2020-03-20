package recursion_and_dynamic_programming;

public class 排成一条线的纸牌博弈问题 {
    public static int win(int[] arr){
        if (arr == null || arr.length == 0){
            return 0;
        }
        if (arr.length == 1){
            return arr[0];
        }
        return Math.max(f(arr, 0, arr.length-1),
                s(arr, 0, arr.length-1));

    }
    public static int f(int[] arr, int start, int end){
        if (start == end){
            return arr[start];
        }
        return Math.max(s(arr, start+1, end)+arr[start], s(arr, start, end-1)+arr[end]);
    }
    public static int s(int[] arr, int start, int end){
        if (start == end){
            return 0;
        }
        return Math.min(f(arr, start+1, end), f(arr, start, end-1));
    }
    public static int dp(int[] arr){
        if (arr == null || arr.length == 0){
            return 0;
        }
        int[][] f = new int[arr.length][arr.length];
        int[][] s = new int[arr.length][arr.length];
        f[0][0] = arr[0];
        s[0][0] = 0;
        for(int j=0; j < arr.length;j++){
            f[j][j] = arr[j];
            for (int i=j-1;i>=0;i--){
                f[i][j] = Math.max(s[i+1][j] + arr[i], s[i][j-1]+arr[j]);
                s[i][j] = Math.min(f[i+1][j] , f[i][j-1]);
            }
        }
        return Math.max(f[0][arr.length-1], s[0][arr.length-1]);
    }

    public static void main(String[] args) {
        System.out.println(dp(new int[]{1,5,2}));
    }
}
