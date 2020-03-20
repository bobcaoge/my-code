package arry_and_matrix_problems;

public class 计算数组的小和 {
    public static int sum = 0;
    public static int calc_sum(int[] nums){

        merge_sort(nums, 0, nums.length-1);
        int ret = sum;
        sum = 0;
        return ret;

    }
    public static int[] merge_sort(int[] nums, int start, int end){
        if(start == end){
            return new int[]{nums[start]};
        }
        int[] left = merge_sort(nums, start, (start+end)/2);
        int[] right = merge_sort(nums, (start+end)/2+1, end);
        int length_of_right = right.length;
        int index_of_left = 0;
        int index_of_right = 0;
        int i=0;
        int[] ret = new int[end-start+1];
        while (index_of_left < left.length && index_of_right < right.length){
            if(right[index_of_right] >= left[index_of_left]){
                sum += left[index_of_left]*(length_of_right-index_of_right);
                ret[i] = left[index_of_left++];
            }else{
                ret[i] = right[index_of_right++];
            }
            i++;
        }
        while( index_of_left < left.length){
            ret[i++] = left[index_of_left++];
        }
        while( index_of_right< right.length){
            ret[i++] = right[index_of_right++];
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(calc_sum(new int[]{1,3,5,2,4,6}));

    }
}
