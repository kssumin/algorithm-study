import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Backjoon_2407 {
    static BigInteger[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        arr = new BigInteger[n + 1][m + 1];

        BigInteger answer = dp(n, m);
        System.out.println(answer);
    }

    private static BigInteger dp(int n, int m) {
        if (arr[n][m] != null) {
            return arr[n][m];
        } else {
            if (m == 1) {
                arr[n][m] = BigInteger.valueOf(n);
                return BigInteger.valueOf(n);
            }
            if (m == 0) {
                arr[n][m] = BigInteger.ONE;
                return BigInteger.valueOf(n);
            }
            if (n == m) {
                arr[n][m] = BigInteger.ONE;
                return BigInteger.ONE;
            } else {
                return dp(n - 1, m - 1).add(dp(n - 1, m));
            }
        }
    }
}
