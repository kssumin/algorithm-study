import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int arr[] = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr); // 오름차순 정렬

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        while (M-- > 0) {
            int target = Integer.parseInt(st.nextToken());
            sb.append(binarySearch(arr, target, 0, N - 1)).append("\n");
        }
        System.out.println(sb);

    }

    private static int binarySearch(int[] arr, int target, int start, int end) {

        if (start > end) {
            return 0;
        }
        int mid = (start + end) / 2;
        if (arr[mid] == target) {
            return 1;
        } else if (arr[mid] > target) {
            return binarySearch(arr, target, start, mid - 1);
        } else {
            return binarySearch(arr, target, mid + 1, end);
        }

    }
}