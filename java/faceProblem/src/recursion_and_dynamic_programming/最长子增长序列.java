package recursion_and_dynamic_programming;

public class 最长子增长序列 {
    public static int[] getdp_1(int[] arr){
        int[] nums = new int[arr.length];
        nums[0] = 1;
        for (int i=1;i<arr.length;i++){
            nums[i] = 1;
            for (int j=0;j<i;j++){
               if( arr[i] > arr[j]){
                   nums[i] = Math.max(nums[j]+1, nums[i]);
               }
            }
        }
        return nums;
    }
    public static int[] getdp(int[] arr){
        int[] dp= new int[arr.length];
        dp[0] = 1;
        int[] ends = new int[arr.length];
        ends[0] = arr[0];
        int right = 0;
        for (int i=1;i<arr.length;i++){
            int start = 0;
            int end = right;
            int mid = (start+end)/2;
            while (start <= end){
                if (ends[mid] < arr[i]){
                    start = mid + 1;
                }else{
                    end = mid - 1;
                }
                mid = (start + end)/2;
            }
            right = Math.max(right, start);
            ends[start] = arr[i];
            dp[i] = start+1;

        }
        for (int end: ends) {
            System.out.print(end+ " ");
        }
        System.out.println();
        return dp;
    }
    public static int[] generateLIS(int[] arr){
        int[] dp = getdp(arr);
        for (int num: dp) {
            System.out.print(num+" ");
        }
        System.out.println();
        int pos = 0;
        int max = 0;
        for (int i=0;i<dp.length;i++){
            if (dp[i] > max){
                pos = i;
                max = dp[i];
            }
        }
        int[] ret = new int[max];
        ret[max-1] = arr[pos];
        int i=pos;
        for (;i>=0;i--){
            if (dp[i]==dp[pos]-1){
                ret[dp[i]-1] = arr[i];
                pos = i;
            }
        }
        return ret;
    }
    public static void main(String[] args){
        int[] result = generateLIS(new int[]{2,1,5,3,6,4,8,9,7});
        for (int num: result) {
            System.out.print(num+" ");
        }
    }
}
