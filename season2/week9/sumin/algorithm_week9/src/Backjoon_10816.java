import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Backjoon_10816 {
    private static List<Integer> answerList;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        String[] answer = br.readLine().split(" ");

        int M = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");

        answerList = Arrays.stream(answer).map(Integer::parseInt).sorted().collect(Collectors.toList());
        List<Integer> inputList = Arrays.stream(input).map(Integer::parseInt).toList();

        for (int i = 0; i < M; i++) {
            sb.append(upperbound(inputList.get(i)) - lowerBound(inputList.get(i)));
            sb.append(" ");
        }
        System.out.println(sb);

    }

    // target보다 크거나 같은 값이 처음 나오는 위치를 찾아야 함
    private static int lowerBound(int target) {
        int left = 0;
        int right = N;

        while (left < right) {
            int mid = (left + right) / 2;

            // 중앙값이 타겟보다 큼
            if (answerList.get(mid) >= target) {
                right = mid;
            }
            // 중앙값이 타켓보다 작음
            else {
                left = mid + 1;
            }
        }
        return left;
    }

    // target보다 큰 값이 처음 나오는 위치를 찾아야 함
    private static int upperbound(int target) {
        int left = 0;
        int right = N;

        while (left < right) {
            int mid = (left + right) / 2;

            //  target보다 작거나 같은 값
            if (answerList.get(mid) <= target) {
                // mid 넢었을 때 작았으니깐 mid 필요 없어
                left = mid + 1;
            }
            // target과 큰 값
            else {
                // mid 넣었을 때 컸으니깐 mid 필요 있어
                right = mid;
            }
        }
        return left;
    }
}
