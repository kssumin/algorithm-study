import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class Solution_11478 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String input = br.readLine();
        HashSet<String> set = new HashSet<>();

        for (int size = 1; size < input.length() + 1; size++) {
            for (int i = 0; i < input.length(); i++) {
                if (i + size <= input.length()) {
                    String substring = input.substring(i, i + size);
                    set.add(substring);
                }
            }
        }

        out.println(set.size());

        br.close();
    }
}
