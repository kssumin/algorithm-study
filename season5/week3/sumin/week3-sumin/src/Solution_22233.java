import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class Solution_22233 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));
        HashSet<String> set = new HashSet<>();

        String[] split = br.readLine().split(" ");
        int N = Integer.parseInt(split[0]);
        int M = Integer.parseInt(split[1]);

        for (int i = 0; i < N; i++) {
            String read = br.readLine();
            set.add(read);
        }

        for (int i = 0; i < M; i++) {
            String[] split1 = br.readLine().split(",");

            for (String s : split1) {
                set.remove(s);
            }
            int size = set.size();
            bw.write(size+"\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
