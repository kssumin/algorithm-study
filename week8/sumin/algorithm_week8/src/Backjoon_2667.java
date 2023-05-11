import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 처음에 시작할 점을 찾는 게 어려웠음
 */
public class Backjoon_2667 {
    static int[][] arr;
    static int n;
    static BufferedReader br;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean[][] isChecked;
    static Map<Integer, Integer> map;
    static int count;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n + 1][n + 1];
        isChecked = new boolean[n + 1][n + 1];
        map = new HashMap<>();
        count = 0;
        StringBuilder sb = new StringBuilder();

        initGraph();

        // 이렇게 시작하는 점이 어려웠다.
        // 시작?? 어?? 시작하는 점도 bfs로 찾아야 하나?
        // 아 ~ 그냥 loop문 돌려서 차례대로 1인 node 찾아야 겠다
        // 이전까지 풀었던 문제는 연결되지 않은 node는 신경 쓸 필요가 없었는데
        // 이 문제는 연결된 노드의 묶음안에 들어있는 수를 알아야 한다.
        // 따라서 한번 연결이 끝났다고 dfs가 끝나면 안 되고 결국엔 n*n을 다 돌면서 반복적으로 dfs를 시작해야 한다.
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (arr[i][j] == 1 && yetVisited(i, j)) {
                    count++;
                    map.put(count, 0);
                    bfs(i, j);
                }
            }
        }

        sb.append(count + "\n");
        for (Integer integer : answer()) {
            sb.append(integer+"\n");
        }

//
        System.out.println(sb);
    }

    private static void initGraph() throws IOException {
        for (int i = 1; i < n + 1; i++) {
            String[] input = br.readLine().split("");
            for (int j = 1; j < n + 1; j++) {
                arr[i][j] = Integer.parseInt(input[j - 1]);
            }
        }
    }

    private static void bfs(int x, int y) {
        map.put(count, map.get(count) + 1);
        isChecked[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int newX = dx[i] + x;
            int newY = dy[i] + y;

            if (isRanged(newX, newY) && arr[newX][newY] == 1 && yetVisited(newX, newY)) {
                bfs(newX, newY);
            }
        }
    }

    private static boolean yetVisited(int newX, int newY) {
        return !isChecked[newX][newY];
    }

    private static boolean isRanged(int newX, int newY) {
        return isRangedWithX(newX) && isRangedWithY(newY);
    }

    private static boolean isRangedWithX(int newX) {
        return newX >= 1 && newX <= n;
    }

    private static boolean isRangedWithY(int newY) {
        return newY >= 1 && newY <= n;
    }

    // 처음에는 ArrayList를 사용했음 -> 동적 배열이니깐 size값을 정하지 않으니 좋다고 생각함
    // 문제점 -> add는 해당 인덱스에 값을 "추가"하는 거임 변경이 아니였음
    // 그래서 map을 사용해서 값을 "변경"으로 바꿈
    private static List<Integer> answer() {
        return map.values().stream()
                .sorted()
                .collect(Collectors.toList());
    }

}

