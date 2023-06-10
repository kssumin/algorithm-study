import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_1535 {
    static int[] lossList;
    static int[] joyList;
    static int N;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N은 몇 번째 사람인지 나타냄
        N = Integer.parseInt(br.readLine());
        arr = new int[N+1][100];

        String[] lossInput = br.readLine().split(" ");
        String[] joyInput = br.readLine().split(" ");

        // 초기화
        for (int i = 0; i < N; i++) {
            int loss = Integer.parseInt(lossInput[i]);
            int joy = Integer.parseInt(joyInput[i]);

            lossList[i] = loss;
            joyList[i] = joy;
        }

        // 기준값 -> 몇 번째 사람?
        for (int i = 0; i < N; i++) {
            // 비교값 -> 체력
            for (int j = 0; j < i; j++) {
                // i번째 사람은 무조건 악수할거임 -> 그러니깐 해당 사람을 만나지 않았을 때의 체력소모는 별값이 없음
                if (lossList[i] <= j) {
                    arr[i][j] = Math.max(arr[i - 1][j - lossList[i]] + joyList[i], arr[i - 1][j]);
                } else {
                    arr[i][j] = arr[i-1][j];
                }
            }
        }
        System.out.print(arr[3][99]);
    }
}
