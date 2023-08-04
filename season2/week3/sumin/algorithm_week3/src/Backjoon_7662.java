import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 처음에는 최댓값, 최솟값을 삭제해야하므로 우선순위 큐를 이용하려고 했다.
 * 그래서 숫자가 높을 수록 우선순위가 높도록 했다.
 * 최댓값을 삭제하는 건 poll()을 통해서 할 수 있었지만
 * 최솟값을 삭제하는 건 기본적으로 주어지는 메서드를 통해서 할수가 없었다.
 * <p>
 * 그럼 기본적으로 주어진 메서드를 이용하기 위해서는 최대힙과 최소힙을 따로 만들고 거기서 poll을 해주면 최댓값 최솟값을 모두 뺄수가 있었다.
 * 근데, 문제에서 Q가 비어있을 경우 D명령이여도 무시를 하고
 * 마지막에 Q가 비어있을 경우 EMPTY를 출력해줘야 한다.
 * <p>
 * 그래서 최댓값 최솟값에서 특정 수를 뺐다는 것을 알 필요가 있었다.
 * 그래야지 만약에 최댓값에서 50이 삭제되었다면 최솟값에서 50을 만나면 이 수는 삭제 된 수라는 걸 기억해야 한다.
 * <p>
 * 하지만 또 다른 문제가 있다.
 * 위 방법에서는 50이 2개라고 하면, 최댓값에서 50을 삭제했을 때 50은 삭제된 수라고 기억하고 있고 그럼 또 다른 50을 최댓값에서조차 삭제할 수가 없다.
 * <p>
 * 방법이 있다.
 * INSET 시에 최대힙, 최소힙에 모두 삽입한다. 또한 Map에 특정 수와 특정수 의 개수를 입력해준다.
 * 이후, DELETE할 때 최대 힙 또는 최소힙에서 삭제를 하고 또한 Map에서 특정 수를 찾아 특정 수의 갯수를 줄여준다.
 * 이렇게 하면 현재 최대 힙 또는 최소 힙에 들어있는 특정 수의 갯수가 몇 개인지 파악할 수 있다.*
 *
 * 이렇게 했는데 실패했다.
 * 신기하게 최대도 123, 최소도 123이 나왔다.
 * 이유는 다음과 같았다.
 * 처음에는 내가 최솟값을 빼고자하면 해당 최솟값이 map에 존재하는지 찾고 없으면 안 빼줬다.
 * 그랬더니 당연히 다음에 또 다음에 최솟값을 빼고자하면 해당 최솟값이 없으니깐 또 최솟값을 못 빼는 상황이 온거다.
 *
 * 1. 그래서 해당 값이 map에 존재하지 않으면 해당 값(최솟값이나 최댓값)을 map에서 빼주고 while문에서 빠져나가게 했다.
 * 어쨋든 우리는 한 개는 빼야하므로
 * 2. 다시 최솟값이나 최댓값을 찾아서 1 과정을 반복했다.(2번 과정 때문에 while문이 필요했다. 아무런 값을 빼지 못했을 경우 다시 값 빼는 과정을 반복하기 위해)
 * 3. 이 와중에 만약 size가 0이 나오면 이제 더 이상 반복을 못하는 것이므로 while문을 빠져나가게 해줬다.
 */
public class Backjoon_7662 {
    private static final String INSERT = "I";
    private static final String DELETE = "D";
    private static Map<Integer, Integer> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer>  min = new PriorityQueue<>();

        //최대힙, 회소힙에 들어있는 값과 해당 값이 몇 개 들어있는지 확인하기 위함
        map = new HashMap<>();

        Integer reply = Integer.parseInt(br.readLine());

        for (int i = 0; i < reply; i++) {
            int k = Integer.parseInt(br.readLine());

            for (int j = 0; j < k; j++) {
                String[] s = br.readLine().split(" ");
                String command = s[0];
                Integer temp = Integer.parseInt(s[1]);
                if (command.equals(INSERT)) {
                    max.add(temp);
                    min.add(temp);
                    map.put(temp, map.getOrDefault(temp, 0) + 1);
//                    System.out.println(temp+" "+map.get(temp));
                }

                if (command.equals(DELETE)) {
                    //최솟값 삭제
                    if (temp == -1) {
                        while (true) {
                            // 존재하는 값을 지우고자 하는 것인지 확인
                            if(canDeleted(min)) {
                                Integer poll = min.poll();
//                                System.out.println("delete 한 값 " + " " + poll);
                                map.put(poll, map.get(poll) - 1);
//                                System.out.println(poll+"개수"+map.get(poll));
                                isZero(poll);
                                break;
                            }
//                            System.out.println("이미 delete한 값");
                            min.poll();
                            if(min.size()==0){
                                break;
                            }
                        }

                    } //최댓값 삭제
                    else {
                        while (true) {
                            if(canDeleted(max)){
                                Integer poll = max.poll();
//                                System.out.println("delete 한 값 "+" "+poll);
                                map.put(poll, map.get(poll) - 1);
//                                System.out.println(poll+"개수"+map.get(poll));
                                isZero(poll);
                                break;
                            }
//                            System.out.println("이미 delete 한 값");
                            max.poll();
                            if(max.size()==0){
                                break;
                            }
                        }
                    }
                }

            }

            if (map.size() == 0) {
                sb.append("EMPTY");
//                System.out.println("왜 나오지?");
                sb.append("\n");
            } else {
                List<Integer> collect = map.keySet().stream().sorted().collect(Collectors.toList());

                sb.append(collect.get(collect.size()-1));
                sb.append(" ");
                sb.append(collect.get(0));
                sb.append("\n");
            }

            map.clear();
            max.clear();
            min.clear();
        }
        System.out.println(sb);
    }

    private static boolean canDeleted(PriorityQueue<Integer> pq) {
        Integer peek = pq.peek();
        if(map.containsKey(peek)){
//            System.out.println("제거 가능합니다");
            return true;
        }
//        System.out.println("제거 불가능");
        return false;
    }

    private static void isZero(Integer poll) {
        if (map.get(poll) == 0) {
//            System.out.println("제거 완료");
            map.remove(poll);
        }
    }
}