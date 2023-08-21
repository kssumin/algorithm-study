package 개인정보수집유효기간;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

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
        String today1 = "2022.05.19";
        String[] terms1 = new String[]{"A 6", "B 12", "C 3"};
        String[] privacies1 = new String[]{"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        int[] answer1 = new int[]{1, 3};
        int[] result1 = new Solution().solution(today1, terms1, privacies1);
        PRINT_RESULT(1, result1, answer1);

        String today2 = "2020.01.01";
        String[] terms2 = new String[]{"Z 3", "D 5"};
        String[] privacies2 = new String[]{"2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"};
        int[] answer2 = new int[]{1, 4, 5};
        int[] result2 = new Solution().solution(today2, terms2, privacies2);
        PRINT_RESULT(2, result2, answer2);
    }

    public static void PRINT_RESULT(int index, int[] result, int[] answer) {
        boolean correct = Arrays.equals(result, answer);
        StringBuilder sb = new StringBuilder();
        sb.append("\n\n테스트 케이스 ").append(index).append(": ");
        sb.append(correct ? "정답" : "오답").append("\n");
        sb.append("\t- 실행 결과: \t").append(result).append("\n");
        sb.append("\t- 기댓값: \t").append(answer).append("\n");
        if (correct) System.out.println(sb);
        else throw new RuntimeException(sb.toString());
    }

    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new LinkedList<>();
        HashMap<String, LocalDate> map = new HashMap<>();

        // today로부터 각 약관이 살아남을 수 있는 최대 시작 date 구하기
        for (String term : terms) {
            String[] s = term.split(" ");
            String key = s[0];
            String value = s[1];

            LocalDate date = LocalDate.parse(today, DateTimeFormatter.ofPattern("yyy.MM.dd"));
            date = date.minusMonths(Long.parseLong(value)).plusDays(1);

            map.put(key, date);
        }

        // 각 privacy마다의 시작 date
        for (int i = 0; i < privacies.length; i++) {
            String[] privacy = privacies[i].split(" ");
            LocalDate date = LocalDate.parse(privacy[0], DateTimeFormatter.ofPattern("yyy.MM.dd"));
            String key = privacy[1];

            // 살아남을 수 있는 최대 시작 date가 각 약관의 시작 date보다 이후이다.
            // 즉 살아남을 있는 최대 시작 date보다 각 약관의 시작 날짜보다 늦다.
            // 즉, 해당 약관은 살아남을 수가 없다,
            if(map.get(key).isAfter(date)){
                answer.add(i+1);
            }
        }
        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}