class Solution {
    public String removeOuterParentheses(String S) {
        String ret = "";
        int num = 0;
        int last = 0;
        for(int i=0;i< S.length();i++){
            if(S.charAt(i) == '('){
                num ++;
            }else{
                num --;
                if(num == 0){
                    ret += S.substring(last+1, i);
                    last = i+1;
                }
            }
        }
        return ret;
    }
    public static void main(String[] args){

        System.out.println(new Solution().removeOuterParentheses("(()())(())"));
    }
}
