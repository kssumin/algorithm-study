import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 처음에 right의 초기값을 N으로 잡았다 => 에러 발생
 * right의 초기값을 N-1으로 줄였더니 해결
 *
 * 이유는?
 * mid 가 N-1에 위치한 값과 동일하다.
 * 그럼 mid 은 더 큰값을 찾아 범위를 줄인다.
 * 하지만 배열[N]에는 값이 없다.
 *
 * 이 부분을 간과했다.
 *
 */
public class Backjoon_19637 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(split[0]);
        int M = Integer.parseInt(split[1]);
        String[][] standard = new String[N][2];

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            standard[i][0] = s[0];
            standard[i][1] = s[1];
        }

        for (int i = 0; i < M; i++) {
            String[] s = br.readLine().split(" ");
            int score = Integer.parseInt(s[0]);
            int left = 0;
            int right = N - 1;

            while (left <= right) {
                int mid = (left + right) / 2;
                int midScore = Integer.parseInt(standard[mid][1]);
                // 비교값이 현재값보다 크거나 같다.
                // 내가 딱 원하는 값이다.
                // 그럼 mid 그 상태로 있어도 될까?
                // 아니다. 더 작은 범위 비교대상 있을 수도 있다.
                // 따라서 해당 경우에도 비교대상 범위를 줄여야 한다.

                // 너무 줄였다. 해당 경우가 나를 수용할 수 있는 min값이였다.(나보다 큰 마지막 경우였다.)
                // 문제가 없다. 방금 case가 마지막이였다면 더 이상 비교대상 값이 작아지지 않을 것이다.
                // 그러면 left는 어느순간 right를 넘을 것이고, 그럼 그 left값이 우리가 찾고자 하는 값이 되는 것이다.
                if (score <= midScore) {
                    right = mid - 1;
                }
                // 비교값이 현재값보다 크다.
                // 나는 비교값이 더 크거나 같으면 좋겠다.
                // 그럼 비교대상 범위를 줄이자!
                else {
                    left = mid  + 1;
                }
            }
            sb.append(standard[left][0]).append("\n");
        }
        br.close();
        System.out.println(sb);
    }
}
