package binaryTreeProblems;

public class Node {
    public int value;
    public Node left;
    public Node right;
    Node(int value){
        this.value = value;
        this.left = null;
        this.right = null;
    }

    @Override
    public String toString() {
        return this.value+" ";
    }
}
