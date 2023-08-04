import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/**
 * EoF(End Of File : 데이터 소스로부터 더 이상 읽을 수 있는 데이터가 없음을 의미)을 처리하는 것이 어려웠다.
 * <p>
 * String input="";
 * //1
 * while((input=br.readLine())!=null){...} : 백준 사이트처럼 입력이 파일로 들어온다면 EOF 처리 가능 하지만 intelliJ에서는 불가능
 * //2
 * while((data = br.readLine()) != null && !data.isEmpty()){...} :  백준 사이트, intelliJ 둘 다 가능 -> enter를 한 번 더 치면 EOF로 처리한다.
 * //3
 * while((data = br.readLine()).equals("")){...} : IntellJ에서는 Enter로 EOF릃 찾을 수 있지만, 백준 사이트처럼 입력 자체가 파일이라면 RuntimeException이 뜬다.(읽을 파일이 없는데 읽은 후 equals를 실행하기 때문)
 */
public class Backjoon_9733 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = {"Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"};

        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String s : str) {
            hashMap.put(s, 0);
        }

        double total = 0;
        String data = "";
        while ((data = br.readLine()) != null && !data.isEmpty()) {
            String[] arr = data.split(" ");
            total += arr.length;
            for (int i = 0; i < arr.length; i++) {
                if (hashMap.containsKey(arr[i])) {
                    hashMap.put(arr[i], hashMap.get(arr[i]) + 1);
                }
            }

        }
        for (int i = 0; i < 7; i++) {
            System.out.printf("%s %d %.2f\n", str[i], hashMap.get(str[i]), hashMap.get(str[i]) / total);
        }
        System.out.printf("%s %d %.2f\n", "Total", (int) total, 1.00);

    }
}
