package string_problems;

public class 翻转字符串 {

    public static char[] rotate_string(char[] words, int pos){
        if (words == null || words.length == 0 || pos <= 0 || pos >= words.length){
            return words;
        }
        int left_start = 0;
        int left_end = pos-1;
        int right_start = pos;
        int right_end = words.length-1;
        int len_left = left_end - left_start+1;
        int len_right = right_end - right_start+1;
        while (len_left !=0 &&  len_right != 0){
//            System.out.println(words);
            if (len_left >= len_right){
                move(words, left_start, left_end, right_start, right_end, true, len_right);
                left_start += len_right;
            }else{

                move(words, left_start, left_end, right_start, right_end, false, len_left);
                right_end -= len_left;
            }
            len_left = left_end - left_start+1;
            len_right = right_end - right_start+1;
        }
        return words;

    }
    public static void move(char[] words, int left_start, int left_end,
                            int right_start, int right_end, boolean move_from_right_to_left, int len){
        char temp;
        if (move_from_right_to_left){
            for (int i=0;i<len;i++){
                temp = words[left_start+i];
                words[left_start+i] = words[right_start+i];
                words[right_start+i] = temp;
            }
        }else{
            for(int i=0;i<len;i++){
                temp = words[left_end-i];
                words[left_end-i] = words[right_end-i];
                words[right_end-i] = temp;
            }
        }
    }
    public static void main(String[] args){
        System.out.println(rotate_string(new char[]{'1','2','3','4','5','6','7','A','B','C','D'}, 5));
    }
}
