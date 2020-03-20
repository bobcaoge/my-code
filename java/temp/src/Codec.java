import java.util.ArrayList;
import java.util.Stack;
class TreeNode{
    public int val;
    public TreeNode left;
    public TreeNode right;
    TreeNode(int x){
        this.val = x;
        this.left = null;
        this.right = null;
    }
    public String toString(){
        return ""+val;
    }

}
public class Codec {
    public TreeNode get_tree(String data){
        if (data.equals("#")){
            return null;
        }
        String[] node_value = data.split(" ");
        TreeNode root = new TreeNode(Integer.parseInt(node_value[0]));
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        for (int i=1;i<node_value.length;i++){
            String value = node_value[i];
            if (stack.peek() != null){
                if (!value.equals("#")){
                    TreeNode buff =  new TreeNode(Integer.parseInt(value));
                    stack.peek().left = buff;
                    stack.push(buff);
                }else{
                    stack.push(null);
                }
            }else{
                if (value.equals("#")){
                    while(stack.peek() == null){
                        stack.pop();
                        stack.pop();
                    }
                    stack.push(null);
                }else{
                    TreeNode buff = new TreeNode(Integer.parseInt(value));
                    TreeNode top = stack.pop();
                    stack.peek().right = buff;
                    stack.push(top);
                    stack.push(buff);
                }
            }
        }
        return root;

    }
    public void traverse(TreeNode root){
        if (root != null){
            System.out.print(root.val+" ");
            traverse(root.left);
            traverse(root.right);
        }
    }
    public ArrayList<Integer> traverse_2(TreeNode root, int length, ArrayList<Integer> al){
        if (root != null){
            if (length>=al.size()){
                al.add(root.val);
            }else{
                al.set(length, root.val);
            }
            System.out.println(length+"  "+ root.val);
            traverse_2(root.right, length +1, al);
            traverse_2(root.left, length+1, al);
        }
        return al;
    }
    public String func(String data){
        TreeNode root = get_tree(data);
        ArrayList<Integer> res = traverse_2(root, 0, new ArrayList<>());
        return "";
    }

    public static void main(String[] args) {
        Codec o = new Codec();
        o.func("1 2 3 # # 6 7 # # # # # # # 8");

    }
}
