import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 이진 탐색 -> 데이터내 특정 값을 정확히 찾는 것
 * lower bound ->  데이터내 특정 K값보다 같거나 큰값이 처음 나오는 위치를 리턴
 * upper bound -> K값보다 처음으로 큰 값이 나오는 위치를 리턴
 *
 *
 * 따라서 지금은 주어진 데이터 내 특정 값이 있는지 없는지를 보면 되기 때문에 이진 탐색을 사용한다.
 */
public class Backjoon_10815 {
    private static List<Integer> answerList;
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        String[] answer = br.readLine().split(" ");
        answerList = Arrays.stream(answer)
                .map(Integer::parseInt)
                .sorted()
                .collect(Collectors.toList());

        int M = Integer.parseInt(br.readLine());
        String[] compare = br.readLine().split(" ");
        List<Integer> compareList = Arrays.stream(compare)
                .map(Integer::parseInt).collect(Collectors.toList());

        for (int i = 0; i < M; i++) {
            sb.append(find(compareList.get(i)));
            sb.append(" ");
        }

        System.out.println(sb);
    }

    private static int find(int target) {
        int left = 0;
        /**
         처음에 N으로 했는데 IndexOutOfBound 에러가 발생함
         근데 만약에 주어진 예시에서 추가적으로 11이 있는지 없는지 찾으려고 하는 경우가 있다고 하자.
         이때 이 값은 주어진 answer값에 없는 값이다.
         하지만 이 값을 찾으려고 결국 index left는 5까지 갈 것이고
         right의 초기값을 n - 1로 했을 경우에는 left>right이기 떄문에 get(mid)를 하지 않지만
         right의 초기값을 n으로 했을 경우에는 아직 left == right이기 때문에 get(5)를 하게 된다.
         이 경우에 IndexOutOfBounds 에러가 발생한다.
         따라서 n-1으로 설정해주어야 한다.
         */

        int right = N - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (answerList.get(mid) == target) {
                return 1;
            } else {
                if (answerList.get(mid) > target) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return 0;
    }
}
