import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Backjoon_11055 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] dp = new int[N];

        String[] s = br.readLine().split(" ");

        // 수열값 초기화
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        // 기준값 -> i
        for (int i = 0; i < N; i++) {
            dp[i] = arr[i];
            // 비교대상 -> j
            for (int j = 0; j < i; j++) {
                // 기준값보다 작은 값이면
                if (arr[i] > arr[j]) {
                    /**
                     * dp는 큰 문제를 작은 문제로 쪼개어 생각해야 한다.
                     * 즉, arr[i] + dp[j] -> 비교대상까지의 수열의 최대합부분과 현재값을 더한다.
                     *
                     * 내가 헷갈렸던 부분은 dp[j]와 더하면 이게 증가하는 부분 수열인지 어떻게 판별하지? 였다.
                     * 왜냐면 조건식 부분은 개별요소가 기준값보다 작은지만 확인하기 때문이다.
                     *
                     * 하지만, 이 또한 dp로 생각한다면 해결이 되는 거였다.
                     */
                    dp[i] = Math.max(arr[i] + dp[j], dp[i]);
                }
            }
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            if (dp[i] > result) {
                result=dp[i];
            }
        }
        System.out.println(result);
    }
}
