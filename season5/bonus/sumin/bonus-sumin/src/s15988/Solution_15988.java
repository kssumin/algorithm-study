package s15988;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_15988 {
    private static final int MOD = 1_000_000_009;
    private static final int LIMIT = 1_000_000;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int reply = Integer.parseInt(br.readLine());

        /**
         * int의 범위는 20억까지이다.
         * 만약, dp[i]가 각각 10억을 넘는다고 하면
         * 다 더했을 때는 30억이 넘는다.
         * 따라서 long 타입으로 선언해야지 오버플로우가 발생하지 않는다.
         *
         * 라고는 하는데.. 왜 여기서 dp[i]가 10억이 넘을 수 있다는 건 어디서 파악하지???
         *
         * 또, 블로그에서 숫자가 커서 나누기를 하는 문제들은 대부분 long으로 바꿔서 풀라고 한다....
         */
        long[] dp = new long[LIMIT + 1];

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i < LIMIT + 1; i++) {
            dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD;
        }

        for (int i = 0; i < reply; i++) {
            int number = Integer.parseInt(br.readLine());
            bw.write(dp[number] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
