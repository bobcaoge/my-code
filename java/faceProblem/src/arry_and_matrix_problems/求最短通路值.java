package arry_and_matrix_problems;

import java.util.LinkedList;
import java.util.Queue;

public class 求最短通路值 {
    public static int min_path(int[][] matrix){
        if(matrix == null || matrix.length == 0||matrix[0].length == 0||
        matrix[0][0] == 0 || matrix[matrix.length-1][matrix[0].length-1] == 0){
            return 0;
        }
        int[][] map = new int[matrix.length][matrix[0].length];
        map[0][0] = 1;
        Queue<Integer> rq = new LinkedList<>();
        Queue<Integer> cq = new LinkedList<>();
        rq.add(0);
        cq.add(0);
        int cr;
        int cc;
        while(!rq.isEmpty()){
            cr = rq.poll();
            cc = cq.poll();
            if(cr == matrix.length-1 && cc == matrix[0].length-1){
                return map[cr][cc];
            }
            walk_to(map[cr][cc], cr+1, cc, rq, cq, map, matrix);
            walk_to(map[cr][cc], cr, cc+1, rq, cq, map, matrix);
            walk_to(map[cr][cc], cr-1, cc, rq, cq, map, matrix);
            walk_to(map[cr][cc], cr, cc-1, rq, cq, map, matrix);
        }
        return 0;
    }
    public static void walk_to(int pre, int to_r, int to_c, Queue<Integer> rq,
                               Queue<Integer> cq, int[][] map, int[][] matrix){
        if(to_r < 0 || to_r >= map.length || to_c <0 || to_c >= map[0].length ||
           map[to_r][to_c] != 0 || matrix[to_r][to_c] != 1){
            return;
        }
        map[to_r][to_c] = pre + 1;
        rq.add(to_r);
        cq.add(to_c);
    }

}
