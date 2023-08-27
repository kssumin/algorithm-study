package 바탕화면정리;

public class Solution {
    public int[] solution(String[] wallpaper) {
        // 시작x, 시작y, 끝x, 끝y
        int lux = Integer.MAX_VALUE, luy = Integer.MAX_VALUE, rdx = 0, rdy = 0;
        for (int i = 0; i < wallpaper.length; i++) {
            String wp = wallpaper[i];
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wp.charAt(j) == '#') {
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    rdx = Math.max(rdx, i + 1);
                    rdy = Math.max(rdy, j + 1);
                }
            }
        }
        return new int[]{lux, luy, rdx, rdy};
    }
}
