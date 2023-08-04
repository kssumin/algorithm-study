import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Backjoon_16953 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] input = br.readLine().split(" ");

        int start = Integer.parseInt(input[0]);
        int last = Integer.parseInt(input[1]);
        int count = 0;

        while (true) {
            if (last % 2 == 0) {
                last = last / 2;
                System.out.println(last);
                count++;
            }
            String s = String.valueOf(last);
            String[] split = s.split("");
            String s1 = split[s.length() - 1];
            if (s1.equals("1")) {
                sb.deleteCharAt(s.length() - 1);
                last = Integer.parseInt(sb.toString());
                System.out.println(last);
                count++;
            }
            if (last == start) {
                break;
            }
            if (last < start) {
                break;
            }
        }
        System.out.println(count);
    }

}
