package recursion_and_dynamic_programming;

public class 矩阵的最小路径和 {
    public static int get_min_sum_of_path(int[][] matrix){
        if (matrix == null){
            return 0;
        }
        for(int i=1;i<matrix.length;i++){
            matrix[i][0] += matrix[i-1][0];
        }
        for(int i=1;i<matrix[0].length;i++){
            matrix[0][i] += matrix[0][i+1];
        }
        for(int i=1;i<matrix.length;i++){
            for (int j=1;j<matrix[0].length;j++){
                matrix[i][j] += Math.min(matrix[i-1][j], matrix[i][j-1]);
            }
        }
        return matrix[matrix.length-1][matrix[0].length-1];
    }
}
