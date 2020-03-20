package string_problems;

import org.omg.Messaging.SYNC_WITH_TRANSPORT;

class MaxHeap{
    public int size;
    public int[] nums;

    public void create(int size){
        if (size < 1){
            return;
        }
        this.size = 0;
        this.nums = new int[size];
    }
    public boolean isEmpty(){
        return this.size == 0;
    }
    public void push(int num){
        if (this.size >= nums.length){
            return;
        }
        this.nums[this.size++] = num;
        int cur = this.size-1;
        for (; cur>0 && num> this.nums[(cur+1)/2-1] ; cur= (cur+1)/2 - 1){
            this.nums[cur] = this.nums[(cur+1)/2-1];
        }
        this.nums[cur] = num;
    }
    public int pop() throws Exception{
        if(this.size <= 0){
            throw new Exception();
        }
        int ret = this.nums[0];
        int temp = this.nums[this.size-1];
        int cur = 0;
        int child = 0;
        this.size --;
        for(;(cur+1)*2-1 < this.size;){
            child = (cur+1)*2-1;
            if((cur+1)*2 < this.size && this.nums[(cur+1)*2] > this.nums[child]){
                child = (cur+1)*2;
            }
            if (this.nums[child] < temp){
                break;
            }
            this.nums[cur] = this.nums[child];
            cur = child;
        }
        this.nums[cur] = temp;
        return ret;
    }
    public void build(int[] nums){
        if (nums == null || nums.length == 0){
            return;
        }
        this.nums = nums;
        for(int i= 0;i<nums.length;i++){
            push(nums[i]);
        }
    }

}
public class 堆排序 {
    public static int[] heap_sort(int[] nums) throws Exception{
        MaxHeap mh = new MaxHeap();
        mh.build(nums);
        for(int i=0;i<mh.size;i++){
            System.out.print(mh.nums[i]+" ");
        }
        System.out.println();
        for(int i=0;i<nums.length;i++){
            int max = mh.pop();
            nums[nums.length-i-1] = max;
        }
        return nums;

    }

    public static void main(String[] args) throws Exception{
        int[] result = heap_sort(new int[]{9,7,2,6,3,1,5});
        for(int i=0;i<result.length;i++){
            System.out.print(result[i]+" ");
        }
        System.out.println();
        /**

        MaxHeap mh = new MaxHeap();
        mh.create(10);
        for(int i=0;i<10;i++){
            mh.push(i);
        }
        for(int i=0;i<mh.size;i++){
            System.out.print(mh.nums[i]+" ");
        }
        try{

            while(!mh.isEmpty()){
                System.out.println(mh.pop());
                for(int i=0;i<mh.size;i++){
                    System.out.print(mh.nums[i]+" ");
                }
                System.out.println();
            }
        }catch (Exception e){

        }

         */
    }
}
