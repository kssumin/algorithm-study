import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_19941 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int length = Integer.parseInt(s[1]);

        String[] split = br.readLine().split("");
        String[] list = new String[N];
        boolean[] alreayAte = new boolean[N];

        for (int i = 0; i < N; i++) {
            list[i] = split[i];
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            if (list[i].equals("P")) {
                int minIndex = Math.max(i - length, 0);
                int maxIndex = Math.min(i + length, N - 1);

                for (int j = minIndex; j <= maxIndex; j++) {
                    if (list[j].equals("H") && !alreayAte[j]) {
                        alreayAte[j] = true;
                        result++;
                        break;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
