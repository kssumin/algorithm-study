import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Backjoon_1427 {
    public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String[] split = br.readLine().split("");
        Collections.sort(Arrays.asList(split), Collections.reverseOrder());
        for (String s : split) {
            out.print(s);
        }

        br.close();
    }
}
