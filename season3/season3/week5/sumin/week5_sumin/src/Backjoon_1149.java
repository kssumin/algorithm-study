import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1. broute force로 접근하려고함 -> 시간초과날 것 같음
 * 2. broute force에 조건을 줘서 O(logn)으로 줄일 수 있을 것 같았음 해당 방법으로 푸려고 함
 * 3. 이전에 어떤 값이 였는지 필요하네? 2번 방법으로 풀면 min값을 비교해서 계속  min값을 업데이트 시켜줌
 * => 결국 이전 값이 필요하고(큰 문제를 풀기위해 작은 문제가 필요함) + 특정 값을 지속적으로 계산해줘야 함
 * 이 부분에서 DP를 떠올리게 됌
 */
public class Backjoon_1149 {
    static int[][] arr;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N + 1][3];

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < 3; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 1; i < N + 1; i++) {
            arr[i][0] = Math.min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0];
            arr[i][1] = Math.min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1];
            arr[i][2] = Math.min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2];
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            if (arr[N][i] < min) {
                min = arr[N][i];
            }
        }

        System.out.println(min);
    }
}
