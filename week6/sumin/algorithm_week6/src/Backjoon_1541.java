import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1. -를 기준으로 분리한다. 그럼 배열의 각 인덱스끼리는 더하고 다른 인덱스끼리는 빼면 된다. -> 즉 첫번째 큰 인덱스는 더하고(55+10) 이후 다오는 인덱스(50+40)은 무조건 빼주면 된다.
 * 실행결과 예1 ) 55-50+40를 input으로 넣었을 때 55 , 50+40 이렇게 분리가 된다.
 * 실행결과 예2 ) 55+10-50+40를 input으로 넣었을 때 55+10 , 50+40 이렇게 분리가 된다.
 * <p>
 * -> 문제 발생 : 이후 55+10인 String에서 55,10을 꺼내려고 빈 문자열을 기준으로 배열을 만들었다. String[] s = input[i].split(""); -> 그랬더니 5,5,+,1,0이 되었다.. 당연한 소리 ㅋ
 * 그래서 55+10을 +을 기준으로 다시 배열로 만들기로 결정했다.
 */
public class Backjoon_1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split("-");
        int answer = 0;
        for (int i = 0; i < input.length; i++) {
            String[] s = input[i].split("\\+");
            for (int j = 0; j < s.length; j++) {
                if (i == 0) {
                    answer += Integer.parseInt(s[j]);
                } else {
                    answer -= Integer.parseInt(s[j]);
                }
            }
        }
        System.out.println(answer);
    }
}
