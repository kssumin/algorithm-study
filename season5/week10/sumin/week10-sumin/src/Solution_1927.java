import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Solution_1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++) {
            int val = Integer.parseInt(br.readLine());

            if(val == 0) {
                if(queue.isEmpty())
                    System.out.println("0");
                else
                    System.out.println(queue.poll());
            }
            else
                queue.add(val);
        }
    }
}
