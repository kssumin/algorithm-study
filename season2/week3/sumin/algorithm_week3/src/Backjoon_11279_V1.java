import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Backjoon_11279_V1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();

        int reply = Integer.parseInt(br.readLine());

        for (int i = 0; i < reply; i++) {
            int input = Integer.parseInt(br.readLine());
            if(input==0){
                if(pq.size()==0){
                    sb.append(0);
                }else{
                    sb.append(pq.poll());
                }
                sb.append("\n");
            }
            else{
                pq.add(input);
            }
        }
        br.close();
        System.out.println(sb.toString());
    }
    /**
     * 우선 이 문제의 제목자체가 최대 힙이여서 최대 힙을 구현해야하겠다고 생각했다.
     * 하지만 최대 힙을 구현하는 방법을 몰랐고
     * 그래서 다시한번 문제를 읽어보니 결국에 우리가 구해야하는 것은 배열에서의 최댓값이였다.
     *
     * 이러한 최댓값을 구하는 방법은 총 3가지 방법이 있을 것 같다.
     * 1. 배열에서 stream을 통해 max값을 찾는다. 하지만 이 경우에는 최댓값을 제거하는 것이 불가능할 것이다.
     * 2. 우선순위 큐를 이용한다. 우선순위 큐에서 x를 기준으로 정렬한다. 우리는 최댓값을 제거해야하므로 우선순위큐는 x가 클수록 우선순위가 높도록 설정해야한다.
     *
     */
}
