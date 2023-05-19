import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Backjoon_7562 {
    static int[][] arr;
    static int[] dx = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] dy = {2, 1, -1, -2, -2, -1, 1, 2};
    static boolean[][] isVisited;
    static int length;
    static int endX;
    static int endY;
    static Queue<Point1> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int reply = Integer.parseInt(br.readLine());
        for (int i = 0; i < reply; i++) {
            length = Integer.parseInt(br.readLine());
            arr = new int[length][length];
            isVisited = new boolean[length][length];
            String[] s1 = br.readLine().split(" ");
            int startX = Integer.parseInt(s1[0]);
            int startY = Integer.parseInt(s1[1]);

            String[] s2 = br.readLine().split(" ");
            endX = Integer.parseInt(s2[0]);
            endY = Integer.parseInt(s2[1]);

            queue = new LinkedList<>();
            queue.add(new Point1(startX, startY, 0));
            isVisited[startX][startY] = true;
            System.out.println(bfs());
        }
    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            Point1 poll = queue.poll();
            if (poll.x == endX && poll.y == endY) {
                return poll.count;
            }
            for (int i = 0; i < 8; i++) {
                int newX = poll.x + dx[i];
                int newY = poll.y + dy[i];

                if (newX >= 0 && newX < length && newY >= 0 && newY < length) {
                    if (!isVisited[newX][newY]) {
                        isVisited[newX][newY] = true;
                        queue.add(new Point1(newX, newY, poll.count + 1));
                    }
                }
            }
        }
        return -1;
    }
}

class Point1 {
    int x;
    int y;
    int count;

    public Point1(int x, int y, int count) {
        this.x = x;
        this.y = y;
        this.count = count;
    }
}
