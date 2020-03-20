package recursion_and_dynamic_programming;

public class N皇后 {
    public static int N_queens_1(int n){
        if (n < 1){
            return 0;
        }
        int[] record = new int[n];
        return process_1(0, record, n);
    }
    public static int process_1(int i, int[] record, int n){
        if (i == n){
            return 1;
        }
        int res = 0;
        for (int j=0;j<n;j++){
            if (isValid(record, i, j)){
                record[i] = j;
                res += process_1(i+1, record, n);
            }
        }
        return res;
    }
    public static boolean isValid(int[] record, int i, int j){
        for(int k=0;k<i;k++){
            if(record[k] == j || Math.abs(k-i) == Math.abs(record[k]-j)){
                return false;
            }
        }
        return true;
    }
    public static int process(int upper, int left, int right, int col){
        if (col == upper){
            return 1;
        }
        int res = 0;
        int pos = upper & (~(left | right | col));
        int most_right = 0;
        while (pos != 0){
            most_right = pos & (~pos + 1);
            pos -= most_right;
            res += process(upper, (left|most_right)<<1, (right|most_right)>>>1, col|most_right);
        }
        return res;
    }

    public static int N_queens(int n){
        if (n < 1){
            return 0;
        }
        int upper = n == 32? -1 : (1<<n) -1;
        return process(upper, 0, 0, 0);
    }
    public static void main(String[] args){
        System.out.println(N_queens(8));

    }
}
