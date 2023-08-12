import java.util.Stack;

class Solution3 {
    public int solution(String s) {
        int answer = 0;

        for(int i = 0; i < s.length(); i++){
            StringBuilder sb = new StringBuilder(s);
            String subString = sb.substring(0, i);
            sb.delete(0,i);
            sb.append(subString);
            if(isString(sb)){
                answer += 1;
            }
        }
        return answer;
    }

    public boolean isString(StringBuilder sb){

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < sb.length(); i++){
            if(stack.isEmpty()){
                stack.push(sb.charAt(i));
            }else{
                if(sb.charAt(i) == ']'){
                    if(stack.peek() == '['){
                        stack.pop();
                    }else{
                        stack.push(sb.charAt(i));
                    }
                }else if(sb.charAt(i) == ')'){
                    if(stack.peek() == '('){
                        stack.pop();
                    }else{
                        stack.push(sb.charAt(i));
                    }
                }else if(sb.charAt(i) == '}'){
                    if(stack.peek() == '{'){
                        stack.pop();
                    }else{
                        stack.push(sb.charAt(i));
                    }
                }else{
                    stack.push(sb.charAt(i));
                }
            }
        }

        if(stack.isEmpty()) return true;
        else return false;

    }
}