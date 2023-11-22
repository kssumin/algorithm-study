import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution1 {
    public int solution(int n, int m, int[] section) {
        int start = section[0];
        int end = section[0] + (m-1);
        int ans = 1;

        for(int i : section){
            if(i>=start && i<=end)
                continue;
            else{
                start = i;
                end = i + (m-1);
                ans++;
            }

        }
        return ans;
    }
}
