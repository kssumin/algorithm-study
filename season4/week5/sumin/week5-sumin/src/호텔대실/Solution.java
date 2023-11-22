package 호텔대실;

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
        String[][] book_time1 = new String[][]{{"15:00", "17:00"}, {"16:40", "18:20"}, {"14:20", "15:20"}, {"14:10", "19:20"}, {"18:20", "21:20"}};
        int answer1 = 3;
        int result1 = new Solution().solution(book_time1);
        PRINT_RESULT(1, result1, answer1);

        String[][] book_time2 = new String[][]{{"09:10", "10:10"}, {"10:20", "12:20"}};
        int answer2 = 1;
        int result2 = new Solution().solution(book_time2);
        PRINT_RESULT(2, result2, answer2);

        String[][] book_time3 = new String[][]{{"10:20", "12:30"}, {"10:20", "12:30"}, {"10:20", "12:30"}};
        int answer3 = 3;
        int result3 = new Solution().solution(book_time3);
        PRINT_RESULT(3, result3, answer3);
    }

    public static void PRINT_RESULT(int index, int result, int answer) {
        boolean correct = result == answer;
        StringBuilder sb = new StringBuilder();
        sb.append("\n\n테스트 케이스 ").append(index).append(": ");
        sb.append(correct ? "정답" : "오답").append("\n");
        sb.append("\t- 실행 결과: \t").append(result).append("\n");
        sb.append("\t- 기댓값: \t").append(answer).append("\n");
        if (correct) System.out.println(sb);
        else throw new RuntimeException(sb.toString());
    }

    private static final int HOUR = 60;
    private static final int MAX_TIME = 1_450;
    private static final int CLEAN_TIME = 10;

    public int solution(String[][] book_time) {
        int answer = 0;

        int[] rooms = new int[MAX_TIME];
        for (String[] time : book_time) {
            String inTime = time[0];
            String outTime = time[1];

            rooms[toTime(inTime)] += 1;
            rooms[toTime(outTime) + CLEAN_TIME] -= 1;
        }

        for (int index = 1; index < rooms.length; index++) {
            rooms[index] += rooms[index - 1];
            answer = Math.max(answer, rooms[index]);
        }

        return answer;
    }

    private static int toTime(String time) {
        String[] split = time.split(":");
        String hour = split[0];
        String minute = split[1];
        return ((Integer.parseInt(hour) * HOUR) + Integer.parseInt(minute));
    }
}