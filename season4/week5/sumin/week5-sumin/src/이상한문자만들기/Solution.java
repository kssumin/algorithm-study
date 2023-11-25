package 이상한문자만들기;

/**
 * main, PRINT_RESULT 는 테스트 케이스 실행 및 결과 확인을 위한 함수입니다.
 * [답안지 복사] 기능을 사용하는 경우 해당 함수들을 제외하며, 답안에 필요한 코드만 복사됩니다.
 * 테스트 케이스 추가 등 함수 내부 변경은 가능하나, 함수 이름 변경시 [답안지 복사] 기능이 제대로 동작하지 않습니다.
 * <p>
 * 또한, 기본 설정으로 [답안지 복사] 사용시 해당 주석과 작성하신 주석을 제외하여 복사됩니다.
 * [주석 복사] 여부는 설정을 통해 변경할 수 있습니다.
 * <p>
 * [도움말 주석] 옵션은 설정을 통해 제거할 수 있습니다.
 * <p>
 * - [답안지 복사]
 * 코드 - 답안지 복사 (기본 단축키 cmd + shift + w)
 * <p>
 * - [도움말 주석]
 * 설정 - 도구 - 프로그래머스 헬퍼 - 도움말 주석
 * <p>
 * - [주석 복사]
 * 설정 - 도구 - 프로그래머스 헬퍼 - 주석 복사
 * <p>
 * GitHub: https://github.com/azqazq195/programmers_helper
 */
class Solution {
    public static void main(String[] args) {
        String s1 = "try hello world";
        String answer1 = "TrY HeLlO WoRlD";
        String result1 = new Solution().solution(s1);
        PRINT_RESULT(1, result1, answer1);
    }

    public static void PRINT_RESULT(int index, String result, String answer) {
        boolean correct = result.equals(answer);
        StringBuilder sb = new StringBuilder();
        sb.append("\n\n테스트 케이스 ").append(index).append(": ");
        sb.append(correct ? "정답" : "오답").append("\n");
        sb.append("\t- 실행 결과: \t").append(result).append("\n");
        sb.append("\t- 기댓값: \t").append(answer).append("\n");
        if (correct) System.out.println(sb);
        else throw new RuntimeException(sb.toString());
    }

    public String solution(String s) {
        StringBuilder answer = new StringBuilder();

        char[] chars = s.toCharArray();
        int idx = 0;

        for (int i = 0; i < chars.length; i++) {
            // 각 단어는 공백문자로 구분한다.
            if (chars[i] == ' ') {
                idx = 0;
            }
            // 짝수인 경우 -> 대문자
            else if (idx % 2 == 0) {
                chars[i] = Character.toUpperCase(chars[i]);
                idx += 1;
            }
            // 홀수인 경우 -> 소문자
            else {
                chars[i] = Character.toLowerCase(chars[i]);
                idx += 1;
            }

            answer.append(chars[i]);
        }
        return answer.toString();
    }
}
/*
  문제를 꼼꼼히 읽어야 한다.

  1. 각 단어는 <br>하나 이상의 공백 문자</br>로 구성되어 있다.
   => 따라서 각 단어의 구분을 split(" ")로 하면 안 된다.

  2. 문자열 전체의 짝/홀수 인덱스 아니라, <br>단어(공백)별로 짝/인수 인덱스를 판단해야 한다.</br>

  즉, 공백은 하나 이상이 아니며, 공백을 만나면 단어를 구분하기 위함이라고 판단하고
  인덱스를 0으로 초기화하여 인덱스를 증가시키면 안 된다.
  또한 공백 이후 문자가 나왔을 때 인덱스를 다시 증가시킨다.
 */