import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Backjoon_16953 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        Integer first = Integer.parseInt(s[0]);
        Integer answer = Integer.parseInt(s[1]);

        LinkedList<Integer> heap = new LinkedList<>();
        int count = 0;
        heap.add(first);
        count++;
        while (true) {
            Integer temp = heap.getLast() * 2;
            if (temp > answer) {
                break;
            } else {
                heap.add(temp);
                count++;
                if(temp.equals(answer)){
                    break;
                }
            }
        }

    }
}
