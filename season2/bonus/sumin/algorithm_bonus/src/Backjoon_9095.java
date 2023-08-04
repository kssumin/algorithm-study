import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * [문제1]
 * 문제 해석을 잘못하고 있었다.
 * 1,2,3으로만 구성할 수 있다!!!!
 * 그래서 초기값 ints[1]=0, ints[2]=1로 잘못설정했다.
 *
 * [문제2]
 * dp -> 큰 문제를 작게 쪼개서 작은 문제 해결법을 저장한 후 큰 문제를 풀 때는 저장한 값을 이용해서 푼다.
 * => 이 방식은 알고 있었지만
 * 어떤 값을 저장해야할지 규칙을 찾기가 힘들었다.
 *
 * [해결방법]
 * +1,+2,+3까지만 가능하다.
 * 그래서 주어진 값 i에서 -1,-2,-3 한 후 각 경우의 수를 더해주면 된다. */
public class Backjoon_9095 {
    static int[] ints = new int[11];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int reply = Integer.parseInt(br.readLine());

        ints[1] = 1;
        ints[2] = 2;
        ints[3] = 4;

        for (int i = 0; i < reply; i++) {
            System.out.println(answer(Integer.parseInt(br.readLine())));
        }
    }

    private static int answer(int i) {
        if (ints[i] != 0) {
            return ints[i];
        }

        return ints[i] = answer(i - 1) + answer(i - 2) + answer(i - 3);
    }
}