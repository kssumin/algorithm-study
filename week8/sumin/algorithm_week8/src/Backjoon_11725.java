import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 1. 인접행렬 -> 메모리 초과가 남
 * 2. LinkedList -> 시간 초과가 남(조회 시간 오래걸림)
 * 3. LinedList<Integer>[] -> 연결이 안 되어 있는 부분은 메모리를 잡아먹지 않음 + 조회도 인덱스로 하기 때문에 빠름
 */
public class Backjoon_11725 {
    //    static int arr[][];
    static List<Integer>[] arr;
    static boolean isChecked[];
    static int node;
    static int[] answer;
    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        node = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        arr = new ArrayList[node + 1];

//        arr = new int[node + 1][node + 1];

//        for (int i = 0; i < node + 1; i++) {
//            arr.add(new LinkedList<>());
//        }

        initGraph();
        isChecked = new boolean[node + 1];
        queue = new LinkedList<>();
        answer = new int[node + 1];

//        for (int i = 0; i < node - 1; i++) {
//            String[] s = br.readLine().split(" ");
//            int x = Integer.parseInt(s[0]);
//            int y = Integer.parseInt(s[1]);
//
//            arr[x][y] = 1;
//            arr[y][x] = 1;
//        }

        for (int i = 0; i < node - 1; i++) {
            String[] s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);

            arr[x].add(y);
            arr[y].add(x);
        }

        queue.add(1);
        isChecked[1] = true;
        dfs();

        for (int i = 2; i < node + 1; i++) {
            sb.append(answer[i] + "\n");
        }

        System.out.println(sb);
    }

    private static void initGraph() {
        for (int i = 1; i < node + 1; i++) {
            arr[i] = new ArrayList<>();
        }
    }

    private static void dfs() {
        while (!queue.isEmpty()) {
            Integer parent = queue.poll();
            List<Integer> connected = isConnected(parent);
            for (Integer next : connected)
                if (yetVisited(next)) {
                    answer[next] = parent;
                    queue.add(next);
                    isChecked[next] = true;
                }
        }
    }


    private static boolean yetVisited(int node) {
        return !isChecked[node];
    }

    private static List<Integer> isConnected(int parent) {
        return arr[parent];
    }


}
