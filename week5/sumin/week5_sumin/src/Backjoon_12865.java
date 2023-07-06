import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_12865 {
    static int N;
    static Integer[][] dp;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] init = br.readLine().split(" ");

        N = Integer.parseInt(init[0]);
        int K = Integer.parseInt(init[1]);

        arr = new int[N + 1][2];
        for (int i = 1; i < N + 1; i++) {
            String[] s = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(s[0]); // weight
            arr[i][1] = Integer.parseInt(s[1]); //value
        }

        dp = new Integer[N + 1][K + 1];
        System.out.println(find(N, K));
    }

    private static Integer find(int i, int k) {
        if (i < 1) {
            return 0;
        }
        if (dp[i][k] != null) {
            return dp[i][k];
        }
        // 목표로 하는 무게가 i번째 아이템의 무게보다도 작다.
        int weight = arr[i][0];
        if (k < weight) {
            dp[i][k] = find(i - 1, k);

        } else {
            int value = arr[i][1];
            dp[i][k] = Math.max(find(i - 1, k), find(i - 1, k - weight) + value);
        }
        return dp[i][k];
    }
}
