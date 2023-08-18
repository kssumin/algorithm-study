import java.util.Arrays;

public class Solution4 {
    public int solution(int[][] routes) {
        int answer = 0;

        Arrays.sort(routes, (route1, route2) -> route1[1] - route2[1]);

        int cam = Integer.MIN_VALUE;

        for(int[] route : routes) {
            if(cam < route[0]) {
                cam = route[1];
                answer++;
            }
        }
        return answer;
    }
}
