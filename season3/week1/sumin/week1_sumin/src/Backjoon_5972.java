import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public class Backjoon_5972 {
    static List<Point>[] list;
    static int[] distance;
    static boolean[] isVisited;
    static int sum = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        list = new LinkedList[n + 1];
        isVisited = new boolean[n + 1];

        for (int i = 0; i < n; i++) {
            list[i] = new LinkedList<>();
        }

        for (int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);

            list[a].add(new Point(b, c));
            list[b].add(new Point(a, c));
        }

        dijkstra(0);
        System.out.println(distance[n]);
    }

    private static void dijkstra(int start) {
        PriorityQueue<Point> queue = new PriorityQueue<>();
        distance[start] = 0;
        queue.add(new Point(start, 0));
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            if (isVisited[point.index]) {
                continue;
            }
            isVisited[point.index] = true;
            for (Point nextPoint : list[point.index]) {
                if (point.cost + nextPoint.cost < distance[point.index]) {
                    distance[point.index] = point.cost + nextPoint.cost;
                    queue.add(new Point(point.index, distance[point.index]));
                    sum += nextPoint.cost;
                }
            }

        }
    }
}

class Point implements Comparable {
    int index;
    int cost;

    @Override
    public int compareTo(Object o) {
        Point point = (Point) o;
        return cost - point.cost;
    }

    public Point(int index, int cost) {
        this.index = index;
        this.cost = cost;
    }
}
