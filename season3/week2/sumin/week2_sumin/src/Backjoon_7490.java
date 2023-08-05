import java.awt.image.ReplicateScaleFilter;
import java.awt.print.Pageable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Backjoon_7490 {
    static boolean[][] isChecked;
    static int N;
    static String[] op = {"+", "-", " "};
    static List<String> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int reply = Integer.parseInt(br.readLine());
        for (int i = 0; i < reply; i++) {
            answer = new LinkedList<>();
            N = Integer.parseInt(br.readLine());
            isChecked = new boolean[2][N];
            dfs(1, "1");
            Collections.sort(answer);

            for (String s : answer) {
                System.out.println(s);
            }
            System.out.println();
        }
    }

    private static void dfs(int num, String s) {
        if (num == N) {
            String replace = s.replace(" ", "");
            // 계산식 계산하기
            calculate(replace, s);
            return;
        }

        // 모든 경우의 계산식 만들기
        for (int i = 0; i < 3; i++) {
            dfs(num + 1, s + op[i] + Integer.toString(num + 1));
        }


    }

    private static void calculate(String express, String original) {
        StringTokenizer st = new StringTokenizer(express, "+|-", true);
        int sum = 0;
        sum += Integer.parseInt(st.nextToken());
        while (st.hasMoreTokens()) {
            if (st.nextToken().equals("+")) {
                sum += Integer.parseInt(st.nextToken());
            } else {
                sum -= Integer.parseInt(st.nextToken());
            }
        }

        if (sum == 0) {
            express.replace("", " ");
            answer.add(original);
        }
    }
}
