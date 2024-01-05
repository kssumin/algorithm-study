package s_3078;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution_3078 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String[] split = br.readLine().split(" ");

        int N = Integer.parseInt(split[0]);
        int K = Integer.parseInt(split[1]);
        Map<Integer, List<Integer>> maps = new HashMap<>();

        long result = 0;

        for (int i = 0; i < N; i++) {
            int currentGrade = i;
            int length = br.readLine().length();

            if (!maps.containsKey(length)) {
                maps.put(length, new ArrayList<>());
            } else {
                List<Integer> list = maps.get(length);
                for (int j = 0; j < list.size(); j++) {
                    if (currentGrade - list.get(j) <= K) {
                        result += list.size();
                        break;
                    } else {
                        list.remove(j--);
                    }
                }
            }
            maps.get(length).add(currentGrade);
        }

        out.println(result);
        br.close();
    }
}