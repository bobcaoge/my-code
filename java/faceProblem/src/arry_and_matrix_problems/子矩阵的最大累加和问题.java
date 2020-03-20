package arry_and_matrix_problems;

public class 子矩阵的最大累加和问题 {
    public static int max_sum(int[][] matrix){
        int ret = Integer.MIN_VALUE;
        for (int i = 0; i <matrix.length; i++) {
            ret = Math.max(ret, max_sum_with_k_rows(matrix, i));
        }
        return ret;
    }
    public static int max_sum_with_k_rows(int[][] matrix, int start_row){
        int max = Integer.MIN_VALUE;
        int[] arr = new int[matrix[0].length];
        for (int i = start_row; i <matrix.length ; i++) {
            add(arr, matrix[i]);
            max = Math.max(max_sum_of_subarray(arr), max);
        }
        return max;
    }
    public static void add(int[] arr, int[] to_add){
        for (int i = 0; i < arr.length ; i++) {
            arr[i] += to_add[i];
        }
    }
    public static int max_sum_of_subarray(int[] arr){
        if(arr == null || arr.length == 0){
            return 0;
        }
        int max = Integer.MIN_VALUE;
        int cur = 0;
        for (int num: arr) {
            cur += num;
            max = Math.max(max, cur);
            cur = cur < 0 ? 0 : cur;
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(max_sum(new int[][]{{-90, 48, 78}, {64, -40, 64},{-81, -7, 66}}));
        System.out.println(max_sum(new int[][]{{-1, -1, -1}, {-1, 2, 2},{-1, -1, -1}}));

    }

}
