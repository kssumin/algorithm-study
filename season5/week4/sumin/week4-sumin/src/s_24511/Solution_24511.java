package s_24511;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_24511 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

        int N = Integer.parseInt(br.readLine());
        Queue<Integer> queue = new LinkedList<>();

        String[] types = br.readLine().split(" ");
        String[] numbers = br.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(numbers[i]);
            int type = Integer.parseInt(types[i]);
            // 스택인 경우
            if (type == 1) {
                // 들어온 값이 나간다.
            }
            // 큐인 경우
            // 이전에 들어온 값이 나가고 들어온 값은 나간다.
            else {
                queue.add(number);
            }
        }

        int reply = Integer.parseInt(br.readLine());
        for (int i = 0; i < reply; i++) {

        }

        bw.flush();
        br.close();
        bw.close();
    }
}
