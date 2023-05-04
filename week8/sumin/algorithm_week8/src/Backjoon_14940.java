import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Backjoon_14940 {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static BufferedReader br;
    static int[][] arr;
    static int[][] answer;
    static boolean[][] isChecked;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        arr = new int[n + 1][m + 1];
        answer = new int[n + 1][m + 1];
        isChecked = new boolean[n + 1][m + 1];

        initGraph();
        Map<String, Integer> start = findStart();
        bfs(start.get("x"), start.get("y"));
        cantNotGo();

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                sb.append(answer[i][j] + " ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    private static void initGraph() throws IOException {
        for (int i = 1; i < n + 1; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 1; j < m + 1; j++) {
                arr[i][j] = Integer.parseInt(line[j - 1]);
            }
        }
    }

    // 목표지점(2) 찾기
    private static Map<String, Integer> findStart() {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (arr[i][j] == 2) {
                    map.put("x", i);
                    map.put("y", j);
                    break;
                }
            }
            break;
        }
        return map;
    }

    private static void bfs(int startx, int starty) {
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(startx, starty));
        isChecked[startx][starty] = true;
        while (!queue.isEmpty()) {
            Point poll = queue.poll();
            int x = poll.getX();
            int y = poll.getY();

            for (int i = 0; i < 4; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];

                if (isRanged(newX, newY) && yetVisited(newX, newY) && canGo(newX, newY)) {
                    queue.offer(new Point(newX, newY));
                    isChecked[newX][newY] = true;
                    answer[newX][newY] = answer[x][y] + 1;
                }
            }
        }
    }

    private static boolean yetVisited(int newX, int newY) {
        return !isChecked[newX][newY];
    }

    private static boolean isRanged(int newX, int newY) {
        return isRangedWithX(newX) && isRangedWithY(newY);
    }

    private static boolean isRangedWithX(int newX) {
        return newX >= 1 && newX <= n;
    }

    private static boolean isRangedWithY(int newY) {
        return newY >= 1 && newY <= m;
    }

    private static boolean canGo(int newX, int newY) {
        return arr[newX][newY] == 1;
    }

    private static void cantNotGo() {
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (canGo(i, j) && !isChecked[i][j]) {
                    answer[i][j] = -1;
                }
            }
        }
    }
}

class Point {
    private int x;
    private int y;

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
