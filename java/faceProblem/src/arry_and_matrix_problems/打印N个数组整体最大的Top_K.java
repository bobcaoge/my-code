package arry_and_matrix_problems;
import tools.Heap;

public class 打印N个数组整体最大的Top_K {
    public static int[] get_K_top_nums(int[] nums, int k){
        if(nums.length <= k){
            return nums;
        }
        Heap heap = new Heap(nums);
        int[] ret = new int[k];
        for (int i = 0; i < k; i++) {
            ret[i] = heap.pop();
        }
        return ret;
    }

    public static void main(String[] args) {
        int[] res = get_K_top_nums(new int[]{1,2,3,4,5,6,7,8}, 3);
        for (int num: res) {
            System.out.print(num+" ");
        }
    }

}
