import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/**
 * [문제상황1]
 * 그리고 문자가 입력받았을 때는 그에 맞는 key(순서)를 보여줘야 하는데,
 * value를 알때, key를 아는 방법은 없었다.
 * 생각해보니 그럴거 같다. 왜냐면 key를 중복없어도 value는 중복이 있으니 value에 맞는 key 값이 여러 개 나올 수 있기 때문이다.
 * 해결방법은 map에 입력할 때 숫자(순서) 문자 / 문자 숫자(순서)를 둘다 입력하는 것이다.
 *
 * [문제상황2]
 * 처음에는 key - 숫자(순서 저장), 문자(문자열)로 사용하였다.
 * 따라서, 숫자/문자를 구분할 필요가 있었는데 해당 부분이 가장 어려웠던 것 같다.
 * 1. [해당 해결 방법을 사용함] Integer.parseInt(String)을 통해 에러 발생하면 false 반환!
 * 2. map에 key,value모두 String으로
 */
public class Backjoon_1620_V1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        HashMap<String, String> map = new HashMap<>();
        String[] s = br.readLine().split(" ");

        int N = Integer.parseInt(s[0]);
        int M = Integer.parseInt(s[1]);

        for (int number = 1; number < N+1; number++) {
            String input = br.readLine();
            map.put(String.valueOf(number), input);
            map.put(input, String.valueOf(number));
        }

        for (int i = 0; i < M; i++) {
            String answer = br.readLine();
            sb.append(map.get(answer));
            sb.append("\n");
        }

        System.out.println(sb.toString());

    }

    private static boolean isNumber(String answer) {
        try {
            int i = Integer.parseInt(answer);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

}
