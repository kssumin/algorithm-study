import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Backjoon_2636 {
    static int M;
    static int N;
    static int[][] arr;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean[][] isChecked;
    static int cheezeCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        M = Integer.parseInt(input[0]);
        N = Integer.parseInt(input[1]);
        arr = new int[M][N];
        isChecked = new boolean[M][N];
        cheezeCount = 0;

        // 총 치즈의 개수
        for (int i = 0; i < M; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                int temp = Integer.parseInt(s[j]);
                arr[i][j] = temp;
                if (temp == 1) {
                    cheezeCount++;
                }
            }
        }
        int answer;

        // 치즈가 남아있지 않다면 작업 종료
        for (answer = 0; isCheese(); answer++) {
            // 초기화 작업
            for (boolean[] arr : isChecked) {
                Arrays.fill(arr, false);
            }

            cheezeCount = 0;
            isChecked[0][0] = true;
            dfs(0, 0);
        }

        System.out.println(answer);
        System.out.println(cheezeCount);

    }

    private static void dfs(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];

            if (newX < 0 || newX >= M || newY < 0 || newY >= N) {
                continue;
            }
            if (!isChecked[newX][newY]) {
                isChecked[newX][newY]=true;
                if (arr[newX][newY] == 1) {
                    arr[newX][newY] = 2;
                    cheezeCount++;
                } else {
                    // 방문하지 않은 점 && 공기
                    dfs(newX, newY);
                }
            }
        }
    }

    private static boolean isCheese() {
        // 공기와 맞닿은 치즈 공기로 바꾸기
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 2) {
                    arr[i][j] = 0;
                }
            }
        }

        // 판 위에 치즈가 존재하는지 체크.
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 1) {
                    return true;
                }
            }
        }
        return false;
    }
}
