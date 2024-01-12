import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class Backjoon_18870 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        StringBuilder sb = new StringBuilder();
        LinkedList<Integer> original = new LinkedList<>();
        LinkedList<Integer> sort = new LinkedList<>();

        int size = Integer.parseInt(br.readLine());

        String[] split = br.readLine().split(" ");
        for (int i = 0; i < size; i++) {
            original.add(Integer.parseInt(split[i]));
            sort.add(Integer.parseInt(split[i]));
        }

        Collections.sort(sort);

        Map<Integer, Integer> maps = new HashMap<>();
        int rank = 0;

        for (Integer i : sort) {
            if (!maps.containsKey(i)) {
                maps.put(i, rank);
                rank++;
            }
        }

        for (Integer i :original) {
            sb.append(maps.get(i)).append(" ");
        }

        out.println(sb);

        br.close();
    }
}
