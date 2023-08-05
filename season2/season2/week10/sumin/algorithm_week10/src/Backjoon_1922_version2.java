import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public class Backjoon_1922_version2 {
    static PriorityQueue<Node> queue = new PriorityQueue<>();
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int com = Integer.parseInt(br.readLine());
        int line = Integer.parseInt(br.readLine());
        parent = new int[com + 1];
        int result = 0; // 가중치의 합

        // 부모 초기 세팅
        for (int i = 1; i < com + 1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < line; i++) {
            String[] input = br.readLine().split(" ");
            int w1 = Integer.parseInt(input[0]);
            int w2 = Integer.parseInt(input[1]);
            int cost = Integer.parseInt(input[2]);

            // 가중치 정렬함
            queue.offer(new Node(w1, w2, cost));
        }

        while (!queue.isEmpty()) {
            Node poll = queue.poll();

            // 부모가 서로 다르다. -> 사이클이 형성되지 않는다
            if (find(poll.w1)!=find(poll.w2)){
                union(poll.w1, poll.w2);
                result+= poll.cost;
            }
        }
        System.out.println(result);
    }

    static private void union(int w1, int w2) {
        int p1 = find(w1);
        int p2 = find(w2);

        // p2의 부모를 p1으로 변경한다.
        if (p1 < p2) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
        }
    }

    // w노드의 부모 노드를 찾는다.
    static private int find(int w) {
        // 부모 노드의 값이 자신이면 자신이 부모노드이다.
        if (parent[w] == w) {
            return w;
        }
        // 부모 노드의 값이 자신이 아니다. 그럴 경우 부모노드의 부모노드를 찾는다.
        return parent[w] = find(parent[w]);
    }
}

class Node implements Comparable<Node> {
    int w1;
    int w2;
    int cost;

    public Node(int w1, int w2, int cost) {
        this.w1 = w1;
        this.w2 = w2;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}
