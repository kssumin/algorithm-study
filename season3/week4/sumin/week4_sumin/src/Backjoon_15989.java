import java.io.*;

public class Backjoon_15989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        int[][] arr = new int[10_001][10_001];
        arr[1][1] = 1; //1

        arr[2][2] = 1; //2
        arr[2][1] = 1; //1+1

        arr[3][3] = 1; //3
        arr[3][2] = arr[1][1]; //1+2
        arr[3][1] = arr[2][1]; //1+1+1

        /**
         * arr[4][1] = arr[3][1] // 1+1+1+1
         * arr[4][2] = arr[2][2] + arr[2][1] // 1+1+1+2 , 1+1+2
         * arr[4][3] = arr[1][1]
         *
         * 여기서만 멈출게 아니다..
         * */

        for (int i = 4; i <= 10_000; i++) {
            arr[i][1] = arr[i - 1][1];
            arr[i][2] = arr[i - 2][2] + arr[i - 2][1];
            arr[i][3] = arr[i - 3][1] + arr[i - 3][2] + arr[i - 3][3];
        }

        for (int i = 0; i < T; i++) {
            int input = Integer.parseInt(br.readLine());
            sb.append(arr[input][1] + arr[input][2] + arr[input][3]).append("\n");
        }
        br.close();
        System.out.println(sb);
    }
}
