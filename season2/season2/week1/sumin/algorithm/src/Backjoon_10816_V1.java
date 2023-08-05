import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Backjoon_10816_V1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        Map<String, Integer> map = new HashMap<>();

        int N = Integer.parseInt(br.readLine());
        String[] hasCard = br.readLine().split(" ");
        for (String x : hasCard) {
            if (map.containsKey(x)) {
                map.put(x, map.get(x) + 1);
            } else {
                map.put(x, 1);
            }
        }

        int M = Integer.parseInt(br.readLine());
        String[] answerCard = br.readLine().split(" ");

        for (String s : answerCard) {
            if(map.containsKey(s)){
                sb.append(map.get(s));
                sb.append(" ");
            }
            else{
                sb.append(0);
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
        br.close();
    }
}
