package arry_and_matrix_problems;

public class 子数组的最大累加和可题 {
    public static int max_sum(int[] nums){
        int max = Integer.MIN_VALUE;
        int cur = 0;
        for (int num : nums) {
            cur = cur < 0 ? 0 : cur;
            cur += num;
            max = Math.max(max, cur);
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(max_sum(new int[]{1,2,3,-4,-5, 1, 1}));

    }
}
