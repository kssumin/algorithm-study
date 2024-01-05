package s_17298;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution_17298 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        String ans = str.substring(0, 1);

        for (int i = 1; i < str.length(); ++i) {
            if (ans.charAt(i - 1) < str.charAt(i)) {
                ans = str.charAt(i) + ans;
            } else {
                ans = ans + str.charAt(i);
            }
        }

        sb.append(ans);
        sb.reverse();
        sb.append("\n");

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}
