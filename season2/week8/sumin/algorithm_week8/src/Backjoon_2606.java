import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Backjoon_2606 {
    static int com;
    static int[][] arr;
    static boolean[] isChecked;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        com = Integer.parseInt(br.readLine());
        int reply = Integer.parseInt(br.readLine());

        arr = new int[com + 1][com + 1];
        isChecked = new boolean[com + 1];
        for (int i = 0; i < reply; i++) {
            String[] s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);
            arr[x][y] = 1;
            arr[y][x] = 1;
        }

        dfs(1);
        System.out.println(countChecked() - 1);

    }

    private static void dfs(int visited) {
        // 방문처리

        isChecked[visited] = true;

        for (int next = 1; next < com + 1; next++) {
            if (isConnected(visited, next) && yetVisited(next)) {
                dfs(next);
            }
        }
    }

//    private static boolean isRanged(int next) {
//        if (next < com) {
//            return false;
//        }
//        return true;
//    }

    private static boolean isConnected(int now, int next) {
        if (arr[now][next] == 1) {
            return true;
        }
        return false;
    }

    private static boolean yetVisited(int next) {
        return !isChecked[next];
    }

    private static int countChecked() {
        int count = 0;
        for (int i = 1; i < com + 1; i++) {
            if (isChecked[i]) {
                count++;
            }
        }
        return count;
    }
}
