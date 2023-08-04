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
         *
         * 자바에서 우선순위 큐는 힙으로 구현되어 있다.
         * 그래서 정렬은 최대힙에 기반으로 정렬되어 있다. 그래서 poll()할 때 index가 1인 가장 큰 값을 반환할 수는 있다.
         * 하지만 반정렬 상태(즉, 정렬은 되어 있지만 부모 자식간의 대소관계에서만 정렬이 되어있는)이기에 우선순위 큐 전체를 보았을 때 정렬이 안 된 것처럼 보이는 것이다.
         *
         * 해당 문제의 우선순위 큐 전체는 다음과 같이 이루어짐
         * [52, 48, 49, 31, 35, 41, 21, 14, 28, 25, 32, 26, 10, 8, 16, 7, 12, 11, 19, 5, 15, 6, 20, 9, 13]
         *
         * 또, 그래서 최대힙을 우선순위 큐로 사용하는 것이 이해가 간다.
         * 만약 배열로 우선순위 큐를 구현한다고 했으면 새로운 값이 들어왔을 때 새로운 값 때문에 밀려난 값들의 인덱스를 변경시켜줘야 하므로 시간복잡도가 O(N)이다.
         * 하지만, 힙으로 구현하기 때문에 새로 들어온 값이 최대로 움질일 수 있는 경우는 힙의 높이이므로 시간복잡도는 O(logN)이다.
         */

//        for (Integer integer : queue.stream().collect(Collectors.toList())) {
//            System.out.println(integer);
//        }
//        System.out.println(queue);


        for(int j=0;j<N-1;j++){
            queue.poll();
        }

        System.out.println(queue.poll());
    }
}
