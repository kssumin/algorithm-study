import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_15662 {
    static boolean[] isChecked;
    static int[][] arr;
    static int T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        arr = new int[T + 1][8];

        // 초기화
        for (int i = 0; i < T; i++) {
            String[] input = br.readLine().split("");
            for (int j = 0; j < 8; j++) {
                arr[i + 1][j] = Integer.parseInt(input[j]);
            }
        }

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            String[] s = br.readLine().split(" ");
            int num = Integer.parseInt(s[0]);
            int direction = Integer.parseInt(s[1]);
            isChecked = new boolean[T + 1];
            start(num, direction);
        }

        int result = 0;
        for (int i = 1; i < T + 1; i++) {
            if (arr[i][0] == 1) {
                result++;
            }
        }
        System.out.println(result);

    }

    private static void start(int num, int direction) {
        isChecked[num] = true;
        rotate(num, direction);

        if (num - 1 >= 1 && !isChecked[num - 1]) {
            if (arr[num - 1][2] != arr[num][6 + direction]) {
                if (direction == 1) {
                    start(num - 1, -1);
                } else {
                    start(num - 1, 1);
                }
            }
        }
        if (num + 1 <= T && !isChecked[num + 1]) {
            if (arr[num + 1][6] != arr[num][direction + 2]) {
                if (direction == 1) {
                    start(num + 1, -1);
                } else {
                    start(num + 1, 1);
                }
            }
        }
    }

    private static void rotate(int num, int direction) {
        // 시계 방향
        if (direction == 1) {
            int temp = arr[num][7];

            for (int i = 7; i >= 1; i--) {
                arr[num][i] = arr[num][i - 1];
            }
            arr[num][0] = temp;
        }
        //반시계 방향
        else {
            int temp = arr[num][0];

            for (int i = 0; i <= 6; i++) {
                arr[num][i] = arr[num][i + 1];
            }
            arr[num][7] = temp;
        }
    }
}
