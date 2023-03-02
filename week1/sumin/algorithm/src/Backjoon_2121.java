import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 집합을 어떻게 저장해야 할지 그 부분에서 막혔다.
 * 또한, 집합들의 모임에 +A, +B한 값이 있는지 확인해야 하는데
 * 처음에는 List<List<Integer>>에서 스트림으로 List<Integer>를 가지고 규칙을 적용해볼까? 라고 생각했는데 코드를 짜지도 못할만큼 복잡했다.
 * 그러다가 생각한 방법이 x,y를 한꺼번에 묶으면 되지 않을까? 라는 생각을 바탕으로 Node 객체를 만들었다.
 * 확실히 이 방법으로 하니 List<Node>에서 하나씩 Node를 꺼내 규칙이 적용된 node들이 있는지 확인하는 과정이 수월했다.
 *
 * 교훈은 복잡하면 객체를 따로 만드는 걸 생각해라!!!
 */
public class Backjoon_2121 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Node> set1 = new HashSet<>();

        int N = Integer.parseInt(br.readLine());

        String[] input = br.readLine().split(" ");
        int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);

        for (int i = 0; i < N; i++) {
            String[] s1 = br.readLine().split(" ");

            Node node = new Node(Integer.parseInt(s1[0]), Integer.parseInt(s1[1]));
            set1.add(node);
        }

        long count = set1.stream()
                .filter(node -> set1.contains(node.plusX(A)) && set1.contains(node.plusY(B)) && set1.contains(node.plusXAndY(A, B)))
                .count();

        System.out.println(count);
    }
}

class Node {
    private int x;
    private int y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Node plusX(int A) {
        return new Node(x + A, y);
    }

    public Node plusY(int B) {
        return new Node(x, y + B);
    }

    public Node plusXAndY(int A, int B) {
        return new Node(x + A, y + B);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Node)) return false;
        Node node = (Node) o;
        return x == node.x && y == node.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}
