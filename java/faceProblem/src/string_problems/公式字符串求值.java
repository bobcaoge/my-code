package string_problems;

import java.util.Deque;
import java.util.LinkedList;

public class 公式字符串求值 {
    public static int get_value(String s){
        return value(s.toCharArray(), 0)[0];
    }
    public static int[] value(char[] chas, int i){
        Deque<String > deque = new LinkedList<>();
        int pre = 0;
        while(i < chas.length && chas[i] != ')'){
            if(chas[i]>='0' && chas[i]<='9'){
                pre = pre*10 + chas[i++]-'0';
            }else{
                if(chas[i] != '('){
                    add_num(deque, pre);
                    deque.addLast(String.valueOf(chas[i++]));
                    pre = 0;
                }else{
                    int[] result = value(chas, i+1);
                    pre = result[0];
                    i = result[1]+1;
                }
            }
        }
        add_num(deque, pre);
        return new int[]{sum(deque), i};
    }
    public static void add_num(Deque<String> deque, int pre){
        if(!deque.isEmpty()){
            String top = deque.pollLast();
            if(top.equals("-") || top.equals("+")){
                deque.addLast(top);
            }else{
                int cur = Integer.valueOf(deque.pollLast());
                pre = top.equals("*")?cur*pre:cur/pre;
            }
        }
        deque.addLast(String.valueOf(pre));
    }
    public static int sum(Deque<String> deque){
        int ret = 0;
        boolean pos = true;
        String top;
        int num ;
        while(!deque.isEmpty()){
            top = deque.pollFirst();
            if(top.equals("-")){
                pos = false;
            }else if(top.equals("+")){
                pos = true;
            }else{
                num = Integer.parseInt(top);
                ret += pos ? num : -num;
            }
        }
        return ret;
    }
    public static void main(String[] args){
        System.out.println(get_value("48*((70-65)-43)+8*1"));
    }
}
