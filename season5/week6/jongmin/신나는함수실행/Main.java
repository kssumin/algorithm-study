package com.study.study.신나는함수실행;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{

    public static int[][][] arr = new int[21][21][21];
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        for(int i=0; i<21; i++){
            for(int j=0; j<21; j++){
                for(int k=0; k<21; k++){
                    if(i==0 || j==0 || k==0) arr[i][j][k] = 1;
                    else if (i<j && j<k) arr[i][j][k] = arr[i][j][k-1] + arr[i][j-1][k-1] - arr[i][j-1][k];
                    else arr[i][j][k] = arr[i-1][j][k]  + arr[i-1][j-1][k] + arr[i-1][j][k-1] - arr[i-1][j-1][k-1];
                }
            }
        }


        while(true){
            String[] strNumbers = bufferedReader.readLine().split(" ");
            int a = Integer.parseInt(strNumbers[0]);
            int b = Integer.parseInt(strNumbers[1]);
            int c = Integer.parseInt(strNumbers[2]);

            if(a==-1 && b==-1 && c==-1) break;
            System.out.println("w("+a+", "+b+", "+c+") = "+w(a,b,c));
        }
    }

    private static int w(int a, int b, int c){
        a = (a>=20) ? 20 : ((a<=0) ? 0 : a);
        b = (b>=20) ? 20 : ((b<=0) ? 0 : b);
        c = (c>=20) ? 20 : ((c<=0) ? 0 : c);
        return arr[a][b][c];
    }
}
