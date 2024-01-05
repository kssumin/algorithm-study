package s1743;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution_1743 {
    static int[][] arr;
    static boolean[][] isChecked;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int N;
    static int M;

    static int count;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String input = br.readLine();
        String[] split = input.split(" ");

        N = Integer.parseInt(split[0]);
        M = Integer.parseInt(split[1]);
        int K = Integer.parseInt(split[2]);

        arr = new int[N + 1][M + 1];
        isChecked = new boolean[N + 1][M + 1];

        for (int i = 0; i < K; i++) {
            String[] split1 = br.readLine().split(" ");
            int x = Integer.parseInt(split1[0]);
            int y = Integer.parseInt(split1[1]);

            arr[x][y] = 1;
        }

        int answer = 0;
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < M + 1; j++) {
                if (arr[i][j] == 1 && !isChecked[i][j]) {
                    count = 0;
                    dfs(i, j);

                    if (count > answer) {
                        answer = count;
                    }
                }
            }
        }
        out.println(answer);
        br.close();
    }

    private static void dfs(int i, int j) {
        count++;
        isChecked[i][j] = true;

        for (int k = 0; k < 4; k++) {
            int newX = i + dx[k];
            int newY = j + dy[k];

            if (newX < 1 || newY < 1 || newX > N || newY > M) {
                continue;
            }

            if (isChecked[newX][newY]) {
                continue;
            }

            if (arr[newX][newY] == 1) {
                dfs(newX, newY);
            }
        }
    }
}
