import java.nio.file.Files;
import java.util.ArrayList;
import java.io.File;

public class dirTree {
    public void get_tree(String path, Node root){
        File file = new File(path); // 获取当前问
        File[] files = file.listFiles();
        for (File f: files){
            if (f.isDirectory()){
                Node cur = new Node(path+"/"+f.getName(), f.getName(), true);
                root.children.add(cur);
                get_tree(cur.path, cur);
            }else{
                root.children.add(new Node(path+"/"+f.getName(), f.getName(), false));
            }
        }
    }
    public Node generate_tree(String path){
        Node root = new Node(path, path, true);
        get_tree(path, root);
        return root;
    }

    public static void main(String[] args) {
        String path = "D:/Project/java/temp";
        dirTree d = new dirTree();
        Node root = d.generate_tree(path);
        d.print_path(root);
    }
    public void print_path(Node root){
        if(root.children.isEmpty()){
            System.out.println(root.path+" " + root.name + " " + root.isDir);
        }else{
            for(Node n: root.children){
                print_path(n);
            }
        }
    }
}
class Node{
    public String  path;
    public String  name;
    public boolean isDir;
    public ArrayList<Node> children = new ArrayList<>();
    public Node(String path, String name, boolean isDir){
        this.path = path;
        this.name = name;
        this.isDir = isDir;
    }
}