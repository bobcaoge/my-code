package tools;

public class Heap {
    public int[] nums;
    public int size;
    public int length;
    public Heap(){
        length = 100;
        nums = new int[100];
    }
    public Heap(int[] nums){
        length = nums.length;
        create(nums);
    }
    public void insert(int to_insert){
        if(this.size < length){
            int index = this.size;
            int father = (index+1)/2 - 1;
            while(index != 0 && nums[father] < to_insert){
               nums[index] = nums[father];
               index = father;
               father = (index+1)/2 - 1;
            }
            nums[index] = to_insert;
        }
        this.size ++;
    }
    public int pop(){
        int ret = nums[0];
        int target = nums[--this.size];
        int cur = 0;
        int left = (cur+1)*2-1;
        int right = left+1;
        int index_of_bigger = cur;
        while(left < this.size){
            if(nums[left] > target){
                index_of_bigger = left;
            }
            if(right < this.size && nums[left] < nums[right]){
                index_of_bigger = right;
            }
            if(index_of_bigger == cur){
                break;
            }
            nums[cur] = nums[index_of_bigger];
            cur = index_of_bigger;
            left = (cur+1)*2-1;
            right = left+1;
        }
        nums[cur] = target;
        return ret;

    }
    public void create(int[] nums){
        this.nums = nums;
        for(int i=0;i<nums.length;i++){
           insert(nums[i]);
        }
    }
    public void print_heap(){
        for (int i = 0; i < this.size; i++) {
            System.out.print(nums[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Heap heap = new Heap(new int[]{1,2,3,4,5,6,7,8});
        while(heap.size > 0){
            System.out.println(heap.pop());
            heap.print_heap();
        }
    }
}
