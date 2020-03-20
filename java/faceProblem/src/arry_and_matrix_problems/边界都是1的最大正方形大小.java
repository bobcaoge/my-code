package arry_and_matrix_problems;

public class 边界都是1的最大正方形大小 {
    public static int max_square(int[][] matrix){
        int ret = 0;
        if (matrix == null){
            return ret;
        }
        int[][] down = new int[matrix.length][matrix[0].length];
        int[][] right = new int[matrix.length][matrix[0].length];
        set_board(down, right, matrix);
        for (int i = 0; i < matrix.length; i++) {
            for (int j  = 0;  j<matrix[0].length ; j++) {
                for (int k = 0; k < Math.min(matrix.length - i, matrix[0].length-j); k++) {
                    if(down[i][j] >= k && right[i][j] >= k && right[i+k][j] >= k && down[i][j+k] >= k){
                        ret = Math.max(ret, k+1);
                    }
                }
            }
        }
        return ret*ret;
    }
    public static void set_board(int[][] down, int[][] right, int[][] matrix){
        if(matrix == null){
            return ;
        }
        int row = matrix.length-1;
        int column = matrix[0].length-1;
        if(matrix[row][column] == 1){
            down[row][column] = 1;
            right[row][column] = 1;
        }
        for (int i = column-1; i >=0 ; i--) {
            if(matrix[row][i] == 1){
                down[row][i] = 1;
                right[row][i] = 1+right[row][i+1];
            }
        }
        for (int i = row-1; i >=0 ; i--) {
            if(matrix[i][column] == 1){
                right[i][column] = 1;
                down[i][column] = 1+down[i+1][column];
            }
        }
        for (int i = row-1; i >=0 ; i--) {
            for (int j = column-1; j >=0 ; j--) {
                if(matrix[i][j] == 1){
                    down[i][j] = 1+down[i+1][j];
                    right[i][j] = 1+right[i][j+1];
                }
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(max_square(new int[][]{{0,1,1,1,1},{0,1,0,0,1},{0, 1,0,0,1},{0,1,1,1,1}, {0,1,0,1,1}}));
    }
}
