import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Backjoon_2644 {
    static boolean[] isChecked;
    static List<Integer>[] graph;
    static int to;
    static int from;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalPerson = Integer.parseInt(br.readLine());
        graph = new LinkedList[totalPerson + 1];
        isChecked = new boolean[totalPerson + 1];

        for (int i = 1; i < totalPerson + 1; i++) {
            graph[i] = new LinkedList<>();
        }

        String[] s = br.readLine().split(" ");
        from = Integer.parseInt(s[0]);
        to = Integer.parseInt(s[1]);
        int m = Integer.parseInt(br.readLine());

        // [ 1. 왜 양방향 관계인거지?]
        // 부모 - 자식 관계를 표현하기 위해서는 단방향으로 표현해야 하는 것이 아닌가

        for (int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]);
            int y = Integer.parseInt(input[1]);
            graph[x].add(y);
            graph[y].add(x);
//            graph.get(x).add(y);
//            graph.get(y).add(x);
        }

        List<Integer> integers = graph[from];
        arr = new int[totalPerson + 1];
        for (Integer integer : integers) {
            if (!isChecked[integer]) {
                arr[integer] = 1;
                dfs(integer);
            }
        }

        if(arr[to]==0){
            System.out.println(-1);
        }
        else{
            System.out.println(arr[to]);
        }

    }

    private static void dfs(Integer integer) {
        isChecked[integer] = true;
        List<Integer> integers = graph[integer];
        for (Integer nextNode : integers) {
//            arr[nextNode] = arr[integer] + 1; -> 이 부분 때문에 이상함
            if (nextNode == to) {
                arr[nextNode] = arr[integer] + 1;
                return;
            }
            if (!isChecked[nextNode]) {
                arr[nextNode] = arr[integer] + 1; //
                dfs(nextNode);
            }
        }
    }
}
