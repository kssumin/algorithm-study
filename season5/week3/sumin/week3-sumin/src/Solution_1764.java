import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class Solution_1764 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String[] split = br.readLine().split(" ");
        int N = Integer.parseInt(split[0]);
        int M = Integer.parseInt(split[1]);

        Set<String> compare = new HashSet<>();
        List<String> answer = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            String read = br.readLine();
            compare.add(read);
        }

        for (int i = 0; i < M; i++) {
            String read = br.readLine();
            if (compare.contains(read)) {
                answer.add(read);
            }
        }

        out.println(answer.size());
        Collections.sort(answer);
        for (String s : answer) {
            out.println(s);
        }

        br.close();
    }
}
