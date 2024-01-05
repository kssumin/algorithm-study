import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Backjoon_1436 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int first = 666;
        while(true) {
            String S = String.valueOf(first);

            for(int i = 0; i < S.length() - 2; i++) {
                if(S.charAt(i) == '6' && S.charAt(i + 1) == '6' && S.charAt(i + 2) == '6') {
                    N--;
                    break;
                }
            }

            if(N == 0) break;
            first++;
        }
        System.out.println(first);
    }
}