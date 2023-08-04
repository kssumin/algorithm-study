import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Backjoon_7576 {
    static int arr[][];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
//    static boolean[][] isVisited;
    static int m;
    static int n;
    static Queue<Point> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        m = Integer.parseInt(s[0]);
        n = Integer.parseInt(s[1]);
        arr = new int[n][m];
//        isVisited = new boolean[n][m];
        queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            String[] s1 = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                Integer tmp = Integer.parseInt(s1[j]);
                arr[i][j]=tmp;
                System.out.print(i+","+j+" ");
                if(tmp==1){
                    queue.add(new Point(i,j));
//                    isVisited[i][j]=true;
                }
            }
            System.out.println();
        }



        dfs();
        int max = date();
        if(max==-1){
            System.out.println(max);
        }
        else{
            System.out.println(max-1);
        }

    }

    private static void dfs() {
        while (!queue.isEmpty()) {
            Point poll = queue.poll();

            for (int i = 0; i < 4; i++) {
                int newX = poll.x + dx[i];
                int newY = poll.y + dy[i];

                if (newX >= 0 && newX < n && newY >= 0 && newY < m) {
                    if (arr[newX][newY]==0) {
                        queue.add(new Point(newX, newY));
                        arr[newX][newY] = arr[poll.x][poll.y] + 1;
                    }
                }
            }
        }
    }

    private static int date() {
        int max = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 0) {
                    return -1;
                }
                if(max<arr[i][j]){
                    max=arr[i][j];
                }
            }
        }
        return max;
    }
}

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
