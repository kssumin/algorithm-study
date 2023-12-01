import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Backjoon_1254 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String input = br.readLine();
        int length = input.length();
        int answer = length;

        for (int i = 0; i < length; i++) {
            if(isPalindrome(input.substring(i))){
                break;
            }
            answer++;
        }

        out.println(answer);

        br.close();
    }

    private static boolean isPalindrome(String substring) {
        int start = 0;
        int last = substring.length() - 1;

        while (start <= last) {
            if (substring.charAt(start) != substring.charAt(last)) {
                return false;
            }
            start++;
            last--;
        }
        return true;
    }
}
