import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Backjoon_2217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> integers = new ArrayList<>();

        // 값 일단 입력하고
        for (int i = 0; i < N; i++) {
            integers.add(Integer.parseInt(br.readLine()));
        }

        /***
         * 이 아래부분이 핵심!
         * 우선 입력받은 값들을 정렬했다.
         */
        Collections.sort(integers);

        int answer=0;
        int temp=0;
        /**
         * 점점 값이 커지므로 두번째 숫자에 맞추면 첫번째 숫자는 포함 안 된다.
         * ex) 4,5,6,7 이면 5,5,5 가능 -> 즉 5*3
         */
        for(int i=0;i<N;i++){
            /**
             * 위에 말한 부분을 여기에서 구현하였다.
             * 첫번째는 N개, 두 번재는 N-1개이다.
             */
            temp=integers.get(i)*(N-i);

            if(temp>answer){
                answer=temp;
            }
        }
        System.out.println(answer);
    }
}
