import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 자연수 S(1 ≤ S ≤ 4,294,967,295) -> int 범위를 넘어가고 long범위는 넘어가지 않는다. 따라서 long 사용
 */
public class Backjoon_1789_V1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());
        System.out.println(find(S, 1));
    }

    private static long find(long S, long total) {
        long n = 1;
        while (true) {
            if (total < S) {
                n++;
                total += n;
                continue;
            }
            if (total == S) {
                return n;
            }
            if (total > S) {
                // 중간에 하나 빼주면 된다.
                return n - 1;
            }
        }
    }
}
