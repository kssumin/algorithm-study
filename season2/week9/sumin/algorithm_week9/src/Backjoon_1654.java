import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Backjoon_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        int K = Integer.parseInt(s[0]);
        long N = Long.parseLong(s[1]);
        long[] arr = new long[K];

        for (int i = 0; i < K; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        long left = 0;
        long right = arr[K - 1] + 1;
        while (left < right) {
            long mid = (left + right) / 2;
            long[] temp = arr.clone();
            long result = 0;

            for (int i = 0; i < K; i++) {
                while (temp[i] - mid >= 0) {
                    temp[i] = temp[i] - mid;
                    result += 1;
                }
            }

            // 원하는 랜선보다 더 많이 가짐 -> 기준치가 낮음 -> 기준치를 높이기
            // 원하는 랜선의 수임 -> 기준치가 적당함
            if (result >= N) {
                left = mid + 1;
            }
            // 원하는 랜섬의 수보다 작음 -> 기준치가 높음 -> 기준치를 낮추기
            //
            else {
                right = mid;
            }
        }

        System.out.println(left - 1);
    }
}
