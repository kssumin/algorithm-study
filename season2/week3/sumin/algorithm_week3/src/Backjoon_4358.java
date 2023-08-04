import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Backjoon_4358 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Map<String, Integer> map = new HashMap();

        String key;
        int total = 0;
        while ((key = br.readLine()) != null && !key.isEmpty()) {
            total++;
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        List<String> list = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String entryKey = entry.getKey();
            list.add(entryKey);
        }

        Collections.sort(list);

        for (String s : list) {
            Double percent = ((double)map.get(s) / (double)total) * 100;

            sb.append(s + " " + String.format("%.4f", percent));
            sb.append("\n");
        }

        System.out.println(sb.toString());
        /**
         * 간단하게 구현했다.
         * 종이의 이름을 key로 하고 해당 종이 이름이 나오는 갯수를 key로 해서 저장했다.
         */
    }
}
