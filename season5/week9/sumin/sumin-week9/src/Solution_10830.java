import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_10830 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());


        long[][] matrix = new long[N][N];
        for(int i=0;i<N;i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long[][] answer = divideCal(matrix,B);

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<N;i++) {
            for(int j=0;j<N;j++) {
                sb.append(answer[i][j]).append(" ");
            }
            sb.setLength(sb.length()-1);
            sb.append("\n");
        }
        System.out.println(sb);
    }


    public static long[][] divideCal(long[][] x, long b ) {

        if(b == 1) {
            for(int i=0;i<x.length;i++) {
                for(int j=0;j<x.length;j++) {
                    x[i][j] = x[i][j] % 1000;
                }
            }
            return x;
        }

        long[][] y = divideCal(x,b/2);
        return (b%2==0)? calProduct(y,y) : calProduct(calProduct(y,y),x);
    }

    public static long[][] calProduct(long[][] m1, long[][] m2) {
        int size = m1.length;

        long temp[][] = new long[size][size];

        for(int i=0;i<size;i++) {
            for(int j=0;j<size;j++) {
                int sum = 0;
                for(int k=0;k<size;k++) {
                    sum += m1[i][k]*m2[k][j];
                }
                temp[i][j] = sum % 1000;
            }
        }

        return temp;
    }


}