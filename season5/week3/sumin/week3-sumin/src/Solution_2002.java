import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Solution_2002 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        List<String> inputs = new LinkedList<>();
        List<Integer> answers = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int i = 0; i < N; i++) {
            String read = br.readLine();
            inputs.add(read);
        }

        for (int i = 0; i < N; i++) {
            String read = br.readLine();
            int inputIndex = inputs.indexOf(read);
            answers.add(inputIndex);
        }

        for (int i = 0; i < N - 1; i++) {
            Integer source = answers.get(i);
            for (int j = i + 1; j < N; j++) {
                Integer compare = answers.get(j);

                if(source > compare){
                    answer++;
                    break;
                }
            }
        }

        out.println(answer);

        br.close();
    }
}
