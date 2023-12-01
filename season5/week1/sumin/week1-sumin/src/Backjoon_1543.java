import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Backjoon_1543 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String find = br.readLine();

        int result = search(input, find);
        System.out.println(result);
    }

    public static int search(String input, String find) {
        int count = 0;
        while (input.length() > 0) {
            if (input.startsWith(find)) {
                count++;
                input = input.substring(find.length());
            } else {
                input = input.substring(1);
            }
        }
        return count;
    }
}
