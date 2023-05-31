import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_11403 {
    static int[][] arr;
    static boolean[] isChecked;
    static int n;
    static int[][] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        answer = new int[n][n];
        isChecked=new boolean[n];

        // 초기화
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(s[j]);
            }
        }

        // i -> j로 가는길 존재하는지 확인
        for (int i = 0; i < n; i++) {
            // i 마다 경로를 탐색해야하므로 방문한 노드 초기화
            for (int j = 0; j < n; j++) {
                isChecked[j] = false;
            }
            // 0 -> 1
            for (int j = 0; j < n; j++) {
                if (arr[i][j] == 1 && !isChecked[j]) {
                    dfs(i, j);
                }
            }
        }


        for (int[] ints : answer) {
            for (int anInt : ints) {
                sb.append(anInt + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    // 0 -> 1
    // 0 -> 2
    // 0 -> 0
    // x -> y 연결되어 있음
    private static void dfs(int x, int y) {
        isChecked[y] = true;

        answer[x][y] = 1;
        for(int next = 0; next < n; next++) {
            // 1 -> 2
            // 2 -> 0
            // y -> next 연결되어 있으면
            if(arr[y][next] == 1 && !isChecked[next]) {
                // 처음에 여기를 dfs(y,next)로 했더니 입력값이랑 동일하게 나옴
                // 우리가 집중해야 할 것은 i에 대해서 갈 수 있는 경로임
                // 즉 x에 대해서 집중해야 함

                // x -> next 연결된 거임
                dfs(x, next);
            }
        }
    }
}
