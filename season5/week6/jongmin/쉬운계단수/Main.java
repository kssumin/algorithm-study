package com.study.study.쉬운계단수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    /*
    길이가 1 : 1 2 3 4 5 6 7 8 9
    길이가 2 : 12 23 34 45 56 67 78 89 10 21 32 43 54 65 76 87 98
    길이가 3 : 121 232 343 454 565 676

    dp[자릿수][끝나는수]
     */

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(bufferedReader.readLine());

        Integer[][] dp = new Integer[101][10];
        dp[1] = new Integer[]{0,1,1,1,1,1,1,1,1,1};



//      바깥쪽 for문은 자릿수를 나타낸다.
        for(int i=2; i<N+1; i++){
//          안쪽 for문은 마지막으로 끝나는 숫자를 나타낸다.
            for(int j=0; j<10; j++){
                if(j==0) dp[i][j] = dp[i-1][1];
                else if (j==9) dp[i][j] = dp[i-1][8];
                else dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];
                dp[i][j] = dp[i][j] % 1_000_000_000;
            }
        }

//        for(Integer[] arr1 : dp){
//            for(Integer arr : arr1){
//                System.out.print(arr+" ");
//            }
//            System.out.println();
//        }

        Integer answer = 0;

        for(Integer a : dp[N]) answer += a;

        System.out.println(answer);
    }
}
