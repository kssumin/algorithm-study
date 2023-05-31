import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Backjoon_9996 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        String target = br.readLine();

        // 문자열 나누기
        String[] str = target.split("\\*");
        for (int i = 0; i < n; i++) {
            String word = br.readLine(); //탐색할 문자
            String start = word.substring(0, str[0].length());
            String end = word.substring(word.length() - str[1].length(), word.length());

            if (word.length() < target.length() - 1) {
                sb.append("NE").append("\n");
                continue;
            }

            if (start.equals(str[0]) && end.equals(str[1])) sb.append("DA").append("\n");
            else sb.append("NE").append("\n");
        }

        System.out.println(sb.toString());
    }
}

