import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Backjoon_2075 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());

        Integer N = Integer.parseInt(br.readLine());

        //queue 용 삽입하기
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                queue.offer(Integer.parseInt(s[j]));
            }
        }

        //왜 우선순위 큐를 list로 변경하면 순서유지가 안 되는 것인가?

//        for (Integer integer : queue.stream().collect(Collectors.toList())) {
//            System.out.println(integer);
//        }


        for(int j=0;j<N-1;j++){
            queue.poll();
        }

        System.out.println(queue.poll());
    }
}
