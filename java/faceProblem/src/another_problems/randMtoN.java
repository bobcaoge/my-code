package another_problems;

public class randMtoN {
    public static int randM(int m){
        return (int)(Math.random()*m+1);
    }

    public static int[] getNmsys(int m, int N){
        int[] ret = new int[32];
        int index = 31;
        while (N>0){
            ret[index] = N%m;
            N /= m;
        }
        return ret;
    }
    public static int[] getMsysNumLessThanN(int[] N, int m){
        int[] res = new int[N.length];
        int start = 0;
        while (N[start] != 0){
            start++;
        }
        int index = start;
        boolean lastEqual = true;
        while (index != N.length){
            res[index] = randM(m) - 1;
            if (lastEqual){
                if (res[index] > N[index]){
                    index = start;
                    continue;
                }else{
                    lastEqual = res[index] == N[index];
                }
            }
            index ++;
        }
        return res;
    }
    public static int getNum(int[] msys, int m){
        int index = msys.length-1;
        int ret = 0;
        while (index >= 0){
            ret = ret*m + msys[index];
            index--;
        }
        return ret;
    }
}
