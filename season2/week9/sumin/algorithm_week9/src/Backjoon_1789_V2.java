import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_1789_V2 {
    private static long S;

    // S가 매우 크기때문에 이진 탐색을 이용해야 한다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = Long.parseLong(br.readLine());
        System.out.println(find());
    }

    // N개의 자연수의 합이 S이다.
    // 이때 자연수 N(갯수)의 최댓값
    private static long find() {
        long start = 1;
        long end = S;
        long answer = 0;

        while (start <= end) {
            long mid = (start + end) / 2;

            // 1 ~ mid 까지의 합
            long total = (mid * (mid + 1)) / 2;

            // 지금까지의 mid의 합이 더 크거나 같다.
            if (total > S) {
                end = mid - 1;
                answer = mid -1 ;
            }
            // 지금까지 mid의 합이 S보다 작다.
            else if(total < S){
                start = mid + 1;
            }
            else{
                end = mid -1;
                answer = mid;
            }
        }
        return answer;
    }
}
