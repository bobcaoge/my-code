package arry_and_matrix_problems;

public class 在行列都排好序的矩阵中找数 {
    public static boolean find(int[][] nums, int k){
        if(nums == null || nums.length == 0){
            return false;
        }
        int row = 0;
        int column = nums[0].length-1;
        while(row < nums.length && column > -1){
            if ( nums[row][column] == k){
                return true;
            }else if (nums[row][column] > k){
                    column --;
            }else{
                row ++;
            }
        }
        return false;
    }
}
