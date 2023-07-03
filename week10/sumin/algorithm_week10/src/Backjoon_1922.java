import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.stream.Collectors;

public class Backjoon_1922 {
    static boolean[] isChecked;
    static List<Edge>[] graph;
    static int computer;
    private static PriorityQueue<Edge> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        computer = Integer.parseInt(br.readLine());
        int line = Integer.parseInt(br.readLine());
        graph = new LinkedList[computer + 1];
        isChecked = new boolean[computer + 1];

        for (int j = 0; j < computer + 1; j++) {
            graph[j] = new LinkedList<>();
        }

        for (int i = 0; i < line; i++) {
            String[] input = br.readLine().split(" ");
            int w1 = Integer.parseInt(input[0]);
            int w2 = Integer.parseInt(input[1]);
            int cost = Integer.parseInt(input[2]);

            graph[w1].add(new Edge(w2, cost));
            graph[w2].add(new Edge(w1, cost));
        }

        queue = new PriorityQueue<>();
        queue.add(new Edge(1, 0));
        int sum = 0;

        while (!queue.isEmpty()) {
            Edge poll= queue.poll();

            // 이미 방문한 점인 경우
            if (isChecked[poll.w]) {
                continue;
            }

            isChecked[poll.w] = true;
            sum += poll.cost;
            for (int i = 0; i < graph[poll.w].size(); i++) {
                Edge nextEdge = graph[poll.w].get(i);
                // 방문하지 않은 정점이라면
                if (!isChecked[nextEdge.w]) {
                    queue.add(new Edge(nextEdge.w, nextEdge.cost));
                }
            }
        }
        System.out.println(sum);
    }
}

class Edge implements Comparable<Edge> {
    int w;
    int cost;

    public Edge(int w, int cost) {
        this.w = w;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return this.cost - o.cost;
    }
}
