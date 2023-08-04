import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Backjoon_1918 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Stack<String> stack = new Stack<>();

        String[] s = br.readLine().split("");

        for (int i = 0; i < s.length; i++) {
            String subject = s[i];
            //피연산자이면
            if (!isOperator(subject)) {
                sb.append(subject);
            }
            //연산자이면
            else {
                //스택이 비어있다면
                if (stack.isEmpty()) {
                    stack.push(subject);
                } else if (subject.equals("(")) {
                    stack.push(subject);
                } else if (subject.equals(")")) {
                    //(가 나올때까지 스택에서 빼고 출력한다. 단, (은 빼기는 하나 출력은 하지 않는다.
                    while (!stack.isEmpty()) {
                        String pop = stack.pop();
                        if (pop.equals("(")) {
                            break;
                        } else {
                            sb.append(pop);
                        }
                    }
                } else {
                    while (!stack.isEmpty()) {
                        //스택 top이 지금 비교하는 연산자보다 우선순위가 더 높다면 스택에서 빼라
                        String peek = stack.peek();
                        if (isFirst(peek) >= isFirst(subject)) {
                            String pop = stack.pop();
                            sb.append(pop);
                        }
                        else{
                            break;
                        }
                    }
                    //넣으려고 하는 연산자의 우선순위가 제일 높음. 또는
                    stack.push(subject);
                }
            }
        }

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        System.out.println(sb);
    }

    private static boolean isOperator(String candidate) {
        if (candidate.equals("*") || candidate.equals("/") || candidate.equals("+") ||
                candidate.equals("-") || candidate.equals("(") || candidate.equals(")")) {
            return true;
        }
        return false;
    }

    private static int isFirst(String s) {
        if (s.equals("+")) {
            return 1;
        }
        if (s.equals("-")) {
            return 1;
        }
        if (s.equals("/")) {
            return 2;
        }
        if (s.equals("*")) {
            return 2;
        }
        return 0;
    }
}