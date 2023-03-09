import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 순서는 중요하지만, 중복은 안 되는 자료구조가 필요했다.
 * Set은 중복이 안 되지만 순서 또한 중요하지 않은 자료구조였고
 * Hash는 key가 없기 때문에 쓸 수 없다고 생각했다.
 * 그래서 LinkedList를 사용했다.
 * <p>
 * 하지만, 시간 초과가 났다.
 * 그래서 Set 인터페이스에서 지원하는 다른 구현 클래스를 찾아보았다.
 * HashSet : 순서대로 입력되지 않고, 중복을 허용하지 않는다.
 * LinkedHashSet : 순서를 보장하고, 중복을 허용하지 않는다.
 * TreeSet : 중복되지 않으면서 특정 규칙에 의해 정렬된 형태의 집합을 쓸 때 사용한다.
 * 자세한 내용은 md 파일에 따로 첨부하겠다.
 * 그래서 지금 상황에서는 LinkedHashSet을 쓰는 게 좋다고 생각했다.
 * 또한, Hash이기 때문에 색인(search) 작업이 빨라 시간초과가 나지 않을 것 같다.
 */
public class Backjoon_13414 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedHashSet<String> list = new LinkedHashSet<>();

        String[] s = br.readLine().split(" ");

        int K = Integer.parseInt(s[0]);
        int L = Integer.parseInt(s[1]);

        for (int i = 0; i < L; i++) {
            String studentId = br.readLine();
            if (list.contains(studentId)) {
                list.remove(studentId);
            }
            list.add(studentId);
        }

        list.stream().limit(K)
                        .forEach(System.out::println);

        br.close();
    }
}
