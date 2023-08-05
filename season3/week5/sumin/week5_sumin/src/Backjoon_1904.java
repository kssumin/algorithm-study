import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 지금 관심있는게 N일 때 나올 수 있는 개수이다.
 * 그럼 우선 개수간의 관계를 파악해보자!
 * <p>
 * [ 변수의 범위 ]
 * int형 범위를 넘어가지 않는다. => 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
 * int형 범위는 대략 20억
 * 따라서 입력N은 int형
 * <p>
 * 배열안의 값도 int형 범위를 넘어갈 수 없다. =>?
 * <p>
 * 1. ArrayOfIndex 발생
 * 왜지? 분명히 입력받은 값보다 +1을 더해서 배열을 생성해주고 있는데 어디서 문제가 발생한거지?
 * 바로 입력을 1로 받으면 arr[2]=1에서 에러가 발생한다. => 배열은 arr[1]까지만 넣을 수 있기 때문
 */
public class Backjoon_1904 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 2];

        arr[1] = 1;
        arr[2] = 2;

        /**
         * 마지막에 나누지 않고 왜 중간중간 연산에서 나누는 거지?
         * 해당 부분을 하지 않으면 실패한다.
         *
         *  % 15746 연산을 어디에서 하느냐에 따라서 결과값도 달라진다.(N = 1_000_000일떄)
         * 그래서 나누기 연산을 마지막에 할 때 이유를 생각해보면 int범위를 넘어가서 오버플로우가 되어 값이 이상해지는 것이다.
         *
         * 이를 방지하기 위해서 (a+b) % d  = (a%d) + (b%d) 라는 성질을 이용한다.
         */
        for (int i = 3; i < N + 1; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
        }

        br.close();
        System.out.println(arr[N]);
    }
}
