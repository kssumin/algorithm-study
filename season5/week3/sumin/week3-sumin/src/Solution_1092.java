import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Solution_1092 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> cranes = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt).collect(Collectors.toList());

        int m = Integer.parseInt(br.readLine());
        List<Integer> boxs = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt).collect(Collectors.toList());

        int answer = 0;
        Collections.sort(cranes, Collections.reverseOrder());
        Collections.sort(boxs, Collections.reverseOrder());

        if (cranes.get(0) < boxs.get(0)) {
            out.println(-1);
            return;
        }

        while (true) {
            if (isZero(boxs)) {
                break;
            }

            for (Integer crane : cranes) {
                for (int i = 0; i < boxs.size(); i++) {
                    if (crane >= boxs.get(i) && boxs.get(i)!=0) {
                        boxs.remove(i);
                        // 해당 컨테이너는 이미 사용했으니깐 다음 컨테이너를 사용해야함
                        break;
                    }
                }
            }
            answer++;
        }
        out.println(answer);

        br.close();
    }

    private static boolean isZero(List<Integer> sources) {
        int sum = sum(sources);

        return sum == 0;
    }

    private static int sum(List<Integer> sources) {
        int sum = 0;
        for (Integer source : sources) {
            sum += source;
        }
        return sum;
    }
}
