package s_1926;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_1926 {
    static int arr[][];
    static boolean isChecked[][];
    static int n;
    static int m;
    static Queue<Point> queue = new LinkedList<>();

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int count;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String[] split = br.readLine().split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);

        arr = new int[n + 1][m + 1];
        isChecked = new boolean[n + 1][m + 1];

        int answer = 0;
        int total = 0;

        for (int i = 1; i < n + 1; i++) {
            String[] split1 = br.readLine().split(" ");
            for (int j = 1; j < m + 1; j++) {
                arr[i][j] = Integer.parseInt(split1[j - 1]);
            }
        }

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (arr[i][j] == 1 && !isChecked[i][j]) {
                    bfs(i, j);

                    // bfs 메서드를 다 실행시켰다는 소리는 queue에 아무 값도 남아있지 않다는 소리이다.
                    // 즉, 더 이상 연결될 그림 조각이 없다는 소리이다.
                    // 그러므로 그림의 갯수를 하나 늘린다.
                    total++;

                    // 그림의 최고 길이를 알기 위해서 현재 가지고 있던 최고 길이인 answer과 비교한다.
                    if (answer < count) {
                        answer = count;
                    }
                }
            }
        }

        out.println(total);
        out.println(answer);
        br.close();
    }

    private static void bfs(int i, int j) {
        count++;
        queue.add(new Point(i, j));
        isChecked[i][j] = true;

        while (!queue.isEmpty()) {
            Point poll = queue.poll();

            int x = poll.getX();
            int y = poll.getY();

            for (int k = 0; k < 4; k++) {
                int newX = x + dx[k];
                int newY = y + dy[k];

                if (newX < 1 || newX > n || newY < 1 || newY > m) {
                    continue;
                }

                if (isChecked[newX][newY]) {
                    continue;
                }

                if (arr[newX][newY] == 1) {
                    queue.add(new Point(newX, newY));
                    isChecked[newX][newY] = true;
                    count++;
                }
            }
        }


    }
}

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
