import java.io.*;

public class Backjoon_1051 {
    static int maxSize = 0;
    static int width = 0;
    static int height = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        height = Integer.parseInt(str[0]);
        width = Integer.parseInt(str[1]);

        String[][] matrix = new String[height][width];

        for (int i = 0; i < height; i++) {
            String[] strs = br.readLine().split("");
            for (int j = 0; j < width; j++) {
                matrix[i][j] = strs[j];
            }
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                for (int size = 0; size + j < width; size++) {
                    squareCheck(matrix, j, i, size);
                }
            }
        }

        System.out.println(maxSize);
    }

    static void squareCheck(String[][] inputMatrix, int x, int y, int size) {
        if (x + size >= width || y + size >= height) {
            return;
        }

        if (inputMatrix[y][x + size].equals(inputMatrix[y][x])) {
            if (inputMatrix[y + size][x].equals(inputMatrix[y][x])) {
                if (inputMatrix[y + size][x + size].equals(inputMatrix[y][x])) {
                    size++;
                    if (maxSize < size * size) {
                        maxSize = size * size;
                    }
                }
            }
        }
    }
}

