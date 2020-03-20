package binaryTreeProblems;

public class 统计和生成所有不同的二叉树 {
    public static int get_nums(int n){
        if (n<2){
            return 0;
        }
        int[] nums = new int[n+1];
        nums[0] = 1;
        for(int i=1;i<nums.length;i++){
            for (int j=1;j<=i;j++){
                nums[i] += nums[j-1]*nums[i-j];
            }
        }
        return nums[nums.length-1];
    }
    public static void main(String[] args){
        System.out.print(get_nums(9));
    }
}
