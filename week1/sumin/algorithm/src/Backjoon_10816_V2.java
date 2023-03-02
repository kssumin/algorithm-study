import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Backjoon_10816_V2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int M = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            int key = Integer.parseInt(st.nextToken());

        }

    }

    //lower bound 찾기(찾고자 하는 key 값의 이상의 값이 처음으로 나타나는 위치)
    private static final int lowerBound(int[] arr, int key) {
        int low = 0;
        int high = arr.length;

        while (low < high) {
            //이분탐색 -> 중앙위치와 key 값을 비교해 lower bound, upper bound를 조정한다.
            int mid = (low + high) / 2;

            if (key <= arr[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    //upper bound 찾기(찾고자 하는 key 값을 초과한 값이 처음으로 나타나는 위치)
    private static int upperBound(int[] arr, int key) {
        int low = 0;
        int high = arr.length;

        // lo가 hi랑 같아질 때 까지 반복
        while (low < high) {

            int mid = (low + high) / 2;

            if (key < arr[mid]) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return high;
    }


}
