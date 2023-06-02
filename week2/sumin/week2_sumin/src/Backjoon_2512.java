import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// 이분 탐색인걸 문제보고 바로 알아차렸는데 문제를 풀고 나니 틀렸습니다. 가 떴다
// 그래서 질문 게시판에서 반례를 보고 디버깅을 통해 고쳤다.
// 이전 코드에서는 result 값을 따로 두지 않고 바로 mid값을 정답으로 반환했다.
// 이때의 문제점은 만약에 sum <= total이여서 mid를 더 키웠는데, mid를 더 키우고 나니 이후에는 모두 sum>total이 되어 문제와 맞지 않았다.
// 그럼에도 불구하고 나는 업데이트가 된 mid값을 반환해서 문제가 있었다.
// 그래서 result 변수를 따로 두고 sum<=total시 mid값을 업데이트 시켜주었다. 일단 이 경우는 문제의 조건을 만족하는 경우이고
// 만약에 또 만족하면서 mid값이 더 크다면 그때 업데이트도 할 수 있고
// 그러지 않는다면 이전에 저장해두었던 mid값이 최대로 줄 수 있는 예산이기 때문이다.
public class Backjoon_2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        String[] s = br.readLine().split(" ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }
        Arrays.sort(arr);
        int total = Integer.parseInt(br.readLine());

        int left = 0;
        int right = arr[N - 1];
        int mid = 0;
        int result = 0;

        while (left <= right) {
            int sum = 0;
            mid = (left + right) / 2;
            for (int want : arr) {
                //원하는 예산이 중앙값보다 적으면 그 값 할당해줌
                if (want <= mid) {
                    sum += want;
                }
                //원하는 예산이 중앙값보다 크면 그냥 중앙값 할당해줌
                else {
                    sum += mid;
                }
            }

            // 총 할당해준 값이 총 예산을 넘어감 -> 그럼 mid의 범위를 줄여야함
            if (sum > total) {
                right = mid - 1;
            }
            //총 할당해준 값이 총 예산보다 같거나 작다 -> 그럼 mid의 범위를 늘려줌
            else {
                result = mid;
                left = mid + 1;
            }
        }
        System.out.println(result);
    }
}
