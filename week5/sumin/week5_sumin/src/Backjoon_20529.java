import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 시간초과 발생
 *
 * MBTI 종류는 총 16가지.
 * 만약, 같은 MBTI가 3개 이상이 있다고 하면 MBTI종류를 볼 필요도 없이 바로 최소 거리는 0이다.
 * 이런식으로 탐색을 줄일 수 있다.
 *
 * [비둘기집 원리]
 * N의 개수만큼 서로 다른 MBTI를 가지고 있다고 했을 때
 * 16까지는 다 다른 MBTI일 것이고
 * 32기까지는 2개씩은 겹칠 것이다.
 * 하지만 33이상인 순간 그때부터는 동일한 MBTI가 3개이상 있을 것이라고 확신할 수 있다.
 *
 *
 */
public class Backjoon_20529 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            if(N>32){
                sb.append(0).append("\n");

                /**
                 * 아래 코드가 없을 때 NumberFormatException이 발생했다.
                 * 어쨋든 MBTI는 입력을 받기 때문에 우리도 읽어야지 다음 부분의 N을 int로 변환할 수 있다.
                 */
                br.readLine();
            }
            else {
                String[] mbti = br.readLine().split(" ");
                sb.append(pick(mbti, N)).append("\n");
            }
        }
        System.out.println(sb);
    }

    private static int pick(String[] mbti, int N) {
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                for (int k = j + 1; k < N; k++) {
                    min = Math.min(min, sumDistance(mbti[i], mbti[j], mbti[k]));
                }
            }
        }
        return min;
    }

    private static int sumDistance(String people1, String people2, String people3) {
        String[] one = people1.split("");
        String[] two = people2.split("");
        String[] three = people3.split("");

        return diff(one, two) + diff(two, three) + diff(three, one);
    }

    private static int diff(String[] one, String[] two) {
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            if (!one[i].equals(two[i])) {
                sum++;
            }
        }
        return sum;
    }
}
