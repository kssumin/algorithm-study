import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 처음엔 값 교환할 때 값 교환하고 다시 원상복구하는 게 귀찮아서
 * 그냥 원래 배열로 얕은 복사해서 거기서 값 교환을 하고 복사한 배열을 GC 대상이 되도록 함
 * -> 메모리 초과 발생
 */
public class Backjoon_3085 {
    static char arr[][];
    static int N;
    static int max = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new char[N][N];

        // 초기화
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        // 행을 기준으로 오른쪽 색과 변경
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - 1; j++) {
                swap(i, j, i, j + 1);
                search();
                swap(i, j + 1, i, j);
            }
        }
        // 열을 기준으로 아래쪽 색과 변경
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < N; j++) {
                swap(i, j, i + 1, j);
                search();
                swap(i + 1, j, i, j);
            }
        }
    }

    public static void swap(int x1, int y1, int x2, int y2) {
        char temp = arr[x1][y1];
        arr[x1][y1] = arr[x2][y2];
        arr[x2][y2] = temp;
    }

    public static void search() {
        // 행에서 긴 수열 탐색
        for (int i = 0; i < N; i++) {
            int count = 1;

            for (int j = 0; j < N - 1; j++) {
                if (arr[i][j] == arr[i][j + 1]) {
                    count++;
                    max = Math.max(count, max);
                } else {
                    count = 1;
                }
            }
        }

        // 열에서 긴 수열 탐색
        for (int i = 0; i < N; i++) {
            int count = 1;

            for (int j = 0; j < N - 1; j++) {
                if (arr[j][i] == arr[j + 1][i]) {
                    count++;
                    max = Math.max(count, max);
                } else {
                    count = 1;
                }
            }
        }
    }
}
