import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

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
        /**
         * 잘못생각하고 있었다. 마치 힙처럼 특정 값이 삽입되면 그에 따라 정렬이 달라지는 줄 알았댜.
         * 우선순위 큐는 우선은 '큐'이다.
         * 그래서 정렬은 삽입된 순서로 되어있고, 대신 poll()할 때 배열에서 가장 큰 값이 찾아서 빼는 것이다.
         *
         * 또, 그래서 최대힙을 우선순위 큐로 사용하는 것이 이해가 간다.
         * 만약 배열로 우선순위 큐를 구현한다고 했으면 새로운 값이 들어왔을 때 새로운 값 때문에 밀려난 값들의 인덱스를 변경시켜줘야 하므로 시간복잡도가 O(N)이다.
         * 하지만, 힙으로 구현하기 때문에 새로 들어온 값이 최대로 움질일 수 있는 경우는 힙의 높이이므로 시간복잡도는 O(logN)이다.
         */

//        for (Integer integer : queue.stream().collect(Collectors.toList())) {
//            System.out.println(integer);
//        }


        for(int j=0;j<N-1;j++){
            queue.poll();
        }

        System.out.println(queue.poll());
    }
}
