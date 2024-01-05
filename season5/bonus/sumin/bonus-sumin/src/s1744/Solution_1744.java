package s1744;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Solution_1744 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> list = new LinkedList<>();
        boolean[] isChecked = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        // 내림차순으로 정렬
        Collections.sort(list, Collections.reverseOrder());

        for (int i = 0; i < list.size(); i++) {
            int current = i;
            int next = i + 1;

            // current 인덱스가 마지막 인덱스일 때
            if (current == list.size() - 1) {
                answer += list.get(current);
                continue;
            }

            // 둘중 하나가 이미 answer 처리한 인덱스이면
            if (isChecked[current] || isChecked[next]) {
                continue;
            }

            // 둘 다 양수일 경우
            if (list.get(current) > 0 && list.get(next) > 0) {
                isChecked[current] = true;
                isChecked[next] = true;
                int temp1 = list.get(current) * list.get(next);
                int temp2 = list.get(current) + list.get(next);

                if (temp1 >= temp2) {
                    answer += temp1;
                } else {
                    answer += temp2;
                }
                continue;
            }

            // 하나는 양수, 하나는 0일 때
            if (list.get(current) > 0 && list.get(next) == 0) {
                // 그 다음 인덱스도 존재할 때, 즉 음수가 하나 더 있을 때는
                if (list.size() - 1 >= next + 1) {
                    isChecked[current] = true;
                    answer += list.get(current);
                }
                // 그 다음 인덱스가 존재하지 않을 때, 즉, 마지막 수 일때는
                else {
                    isChecked[current] = true;
                    isChecked[next] = true;
                    answer += list.get(current) + list.get(next);
                }
                continue;
            }

            // 하나는 0, 다음은 음수일 때
            if (list.get(current) == 0 && list.get(next) < 0) {
                // 남아있는 인덱스가 홀 수 일때
                int rest = (list.size() - 1) - next;
                if (rest % 2 != 0) {
                    isChecked[current] = true;
                    isChecked[next] = true;
                    answer += list.get(current) * list.get(next);
                }
                // 남아있는 인덱스가 짝수 일때
                else {
                    isChecked[current] = true;
                    answer += list.get(current);
                }
                continue;
            }

            // 둘 다 음수일때
            if (list.get(current) < 0 && list.get(next) < 0) {
                isChecked[current] = true;
                isChecked[next] = true;
                answer += list.get(current) * list.get(next);
            }
        }
        out.println(answer);
        br.close();
    }
}
