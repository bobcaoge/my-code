import com.alibaba.fastjson.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class PathToTreeUtil  {
    public  static String getType(String filename, String path){
        if(path.endsWith(filename)){
            return "file";
        }
        return "folder";
    }
    public static void addPath(HashMap<String, Object> root, String path){
        String url = "";
        //将双引号去掉，将多余的空字符去掉
        path = path.replaceAll("\"", "").replaceAll(" ","");
        for (String name:path.split("/")) {
            System.out.println(name);
            url += "/"+name;
            boolean flag = true;
            for (HashMap<String, Object> node: (ArrayList<HashMap<String, Object>>)root.get("content")) {
                if (node.get("name") == name){
                    root = node;
                    flag = false;
                    break;
                }
            }
            if (flag){
                HashMap<String, Object> new_node = new HashMap<>();
                new_node.put("name", name);
                new_node.put("type", getType(name, path));
                new_node.put("url", url);
                new_node.put("content", new ArrayList<HashMap<String, Object>>());
                ((ArrayList<HashMap<String, Object>>)root.get("content")).add(new_node);
                root = new_node;
            }
        }
    }

    public static HashMap<String, Object> generate_data(String s){
        /**
         * 获取[]中的数据
         */

        String [] paths = s.split(",");
        HashMap<String, Object> root =new HashMap<>();
        root.put("name","");
        root.put("url","");
        root.put("type","");
        ArrayList<String> arrayList =new ArrayList<>();
        root.put("content",arrayList );
        for(String path : paths){
            addPath(root, path);
        }
        return root;
    }
    public static String readFile(String pathname) throws Exception{
        String str="";
        File file=new File(pathname);
        try {
            FileInputStream in=new FileInputStream(file);
            // size  为字串的长度 ，这里一次性读完
            int size=in.available();
            byte[] buffer=new byte[size];
            in.read(buffer);
            in.close();

            str=new String(buffer,"GB2312");
        } catch (IOException e) {
            // TODO Auto-generated catch block
            return null;

        }

        return str;


    }

    /****
     * 1. 主分析程序，拿到路径总的字符串，进行分析
     * @param path
     * @return
     */
    public static HashMap<String, Object>   path2json(String path){
        HashMap<String, Object> root;
        root =generate_data(path);
        return  root;
    }


    public  static String mainFunction() throws Exception {
        String file =readFile("D:\\a.txt");
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("data", path2json(file));
        return jsonObject.toString();
    }
    public static void main(String[] args) throws Exception {
        System.out.println(mainFunction());
    }

}
