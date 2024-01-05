package s_2346;

import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution_2346 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        Deque<Ballon> queue = new ArrayDeque<>();
        String[] split = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            queue.addLast(new Ballon(i + 1, Integer.parseInt(split[i])));
        }

        Ballon ballon = queue.removeFirst();
        sb.append(ballon.getIndex() + " ");
        while (!queue.isEmpty()) {
            int index = ballon.getNumber();

            if (index < 0) {
                for (int i = 1; i < -index; i++) {
                    Ballon last = queue.removeLast();
                    queue.addFirst(last);
                }
                ballon = queue.removeLast();
            } else {
                for (int i = 1; i < index; i++) {
                    Ballon first = queue.removeFirst();
                    queue.addLast(first);
                }
                ballon = queue.removeFirst();
            }

            sb.append(ballon.getIndex() + " ");
        }

        out.println(sb);
    }
}

class Ballon {
    int index;
    int number;

    public Ballon(int index, int number) {
        this.index = index;
        this.number = number;
    }

    public int getIndex() {
        return index;
    }

    public int getNumber() {
        return number;
    }
}
