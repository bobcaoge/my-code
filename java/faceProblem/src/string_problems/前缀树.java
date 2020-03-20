package string_problems;

class Node{
    public int path;
    public int end;
    public Node[] nodes;
    Node(){
        path = 0;
        end = 0;
        nodes = new Node[26];
    }

}
public class 前缀树 {

    public Node head = new Node();
    public void insert(String to_insert){
        char[] chars = to_insert.toCharArray();
        Node cur = this.head;
        Node next;
        for(char c: chars){
            next = cur.nodes[c];
            if (next != null){
                next.path ++;
                cur = next;
            }else{
                cur.nodes[c] = new Node();
                cur = cur.nodes[c];
            }
        }
        cur.end ++;
    }
    public void delete(String to_insert){
        if(!find(to_insert)){
            return;
        }
        char[] chars = to_insert.toCharArray();
        Node cur = this.head;
        Node next;
        for(char c: chars){
            next = cur.nodes[c];
            if (next != null){
                next.path --;
                cur = next;
            }else{
                break;
            }
        }
        cur.end --;
    }
    public boolean find(String to_find){
        char[] chars = to_find.toCharArray();
        Node cur = this.head;
        Node next;
        for(char c: chars){
            next = cur.nodes[c];
            if (next != null){
                cur = next;
            }else{
                return false;
            }
        }
        return cur.end > 0;
    }
    public int prefix_number(String to_find){
        if (to_find.length() == 0){
            return head.nodes[0] != null ? head.nodes[0].path:0;
        }
        char[] chars = to_find.toCharArray();
        Node cur = this.head;
        Node next;
        int ret = Integer.MAX_VALUE;
        for(char c: chars){
            next = cur.nodes[c];
            if (next != null){
                ret = Math.min(next.path, ret);
                cur = next;
            }else{
                return 0;
            }
        }
        return ret == Integer.MAX_VALUE ? 0 : ret;
    }
}
