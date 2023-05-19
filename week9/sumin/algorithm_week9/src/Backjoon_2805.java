import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Backjoon_2805 {
    private static int N;
    //최소 M은 가져가야 함. (M 이상)
    private static long M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);

        String[] answer = br.readLine().split(" ");
        int[] answerList = new int[N];

        for (int i = 0; i < N; i++) {
            answerList[i] = Integer.parseInt(answer[i]);
        }

        Arrays.sort(answerList);
        System.out.println(find(answerList));
    }

    // upper bound (target)보다 큰 값중 제일 작은 값
    // upper bound 와는 다른 점은
    // 우선은 M보다 큰 가장
    private static int find(int[] answerList) {
        int left = 1;
        int right = answerList[N - 1];
        int[] temp;
        int mid;

        while (left < right) {
            mid = (left + right) / 2;
            temp = answerList.clone();

            for (int i = 0; i < N; i++) {
                if (temp[i] > mid) {
                    temp[i] = temp[i] - mid;
                } else {
                    temp[i] = 0;
                }
            }

            long result = 0;
            for (int i = 0; i < N; i++) {
                result += temp[i];
            }

            // 너무 H가 높아서 최종 길이가 작다 -> 기준치(높이)를 내리기
            if (result < M) {
                right = mid;
            }
            // 너무 H가 낮아서 최종 길이가 크거나 같다 -> 기준치(높이)를 높여야 함
            else {
                left = mid + 1;
            }
        }
        // left 와 right가 동일한 시점에 멈춘다.
        // 이때 left, right는 M보다 큰 값을 같게 해주는 가중치 지점이다.
        return left - 1;
    }

}
