package s15988;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_15988_v2 {
    private static final int MOD = 1_000_000_009;
    private static final int LIMIT = 1_000_000;
    private static long[] dp;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int reply = Integer.parseInt(br.readLine());
        dp = new long[LIMIT + 1];

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 0; i < reply; i++) {
            int number = Integer.parseInt(br.readLine());
            long result = execute(number);
            bw.write(result + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    /**
     * @param n
     * @return
     */
    private static long execute(int n) {
        if (dp[n] != 0) {
            return dp[n];
        }

        dp[n] = execute(n - 3) + execute(n - 2) + execute(n - 1) % MOD;
        return dp[n];
    }
}
