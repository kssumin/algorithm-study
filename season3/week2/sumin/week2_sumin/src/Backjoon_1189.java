import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 이건 내가 백트래킹인 걸 알았는데
 * 문제는 범위를 계속 잘 못 잡고 있었음....
 * 입력을 1부터 받았는데
 * bfs에서 범위 확인할 때 0부터 확인하고 있었음......
 * 그래서 입력 예제는 통과했는데 백준에서는 통과못함
 * 저 부분을 찾느라 오래걸림..
 */
public class Backjoon_1189 {
    static String[][] arr;
    static boolean[][] isChecked;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static int R;
    static int C;
    static int K;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        R = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);
        K = Integer.parseInt(s[2]);
        arr = new String[R + 1][C + 1];
        isChecked = new boolean[R + 1][C + 1];

        for (int i = 1; i < R + 1; i++) {
            String[] input = br.readLine().split("");
            for (int j = 1; j < C + 1; j++) {
                String s1 = input[j - 1];
                if (s1.equals("T")) {
                    isChecked[i][j] = true;
                }
                arr[i][j] = s1;
            }
        }
        isChecked[R][1] = true;
        bfs(R, 1, 1);
        System.out.println(count);
    }

    private static void bfs(int r, int i, int depth) {
        if (r == 1 && i == C) {
            if (depth == K) {
                count += 1;
            }
            return;
        }

        for (int j = 0; j < 4; j++) {
            int newX = r + dx[j];
            int newY = i + dy[j];

            if (newX < 1 || newY < 1 || newX > R || newY > C) {
                continue;
            }
            if (isChecked[newX][newY]) {
                continue;
            }

            isChecked[r][i] = true;
            bfs(newX, newY, depth + 1);
            isChecked[newX][newY] = false;
        }
    }
}
