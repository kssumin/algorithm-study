import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_9184 {
    static int[][][] arr = new int[21][21][21];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

        while (true) {
            String[] split = br.readLine().split(" ");
            int a = Integer.parseInt(split[0]);
            int b = Integer.parseInt(split[1]);
            int c = Integer.parseInt(split[2]);

            if (a == -1 && b == -1 && c == -1) {
                break;
            }
            int result = dp(a, b, c);
            sb.append("w(" + a + ", " + b + ", " + c + ") = " + result);
            sb.append("\n");
        }

        bw.write(sb.toString());

        bw.flush();
        br.close();
        bw.close();
    }

    private static int dp(int a, int b, int c) {
        // 범위 안에 들고 값이 저장되어 있는 경우
        if (isRanged(a, b, c) && arr[a][b][c] != 0) {
            return arr[a][b][c];
        }
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1;
        }
        if (a > 20 || b > 20 || c > 20) {
            return dp(20, 20, 20);
        }
        if (a < b && b < c) {
            return arr[a][b][c] = dp(a, b, c - 1) + dp(a, b - 1, c - 1) - dp(a, b - 1, c);
        }
        return arr[a][b][c] = dp(a - 1, b, c) + dp(a - 1, b - 1, c) + dp(a - 1, b, c - 1) - dp(a - 1, b - 1, c - 1);
    }

    private static boolean isRanged(int a, int b, int c) {
        return a > 0 && a <= 20 && b > 0 && b <= 20 && c > 0 && c <= 20;
    }
}
