package binaryTreeProblems;
import java.lang.Math;

public class 统计完全二叉树的节点数 {
    public static int get_the_number_of_nodes_of_a_full_tree(Node root){
        if (root == null){
            return 0;
        }
        return traverse(root, 1, get_most_left(root, 1));

    }
    private static int traverse(Node head, int l, int h){
        if (head == null){
            return 0;
        }
        if (get_most_left(head.right, l+1) == h){
            return traverse(head.right, l+1, h) + 1<<(h-l);
        }else{
            return traverse(head.left, l+1, h)+1<<(h-l-1);
        }
    }
    private static int get_most_left(Node head, int cur_level){
        while (head != null){
            cur_level += 1;
            head = head.left;
        }
        return cur_level-1;
    }

}
