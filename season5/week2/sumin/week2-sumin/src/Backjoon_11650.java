import static java.lang.System.in;
import static java.lang.System.out;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Backjoon_11650 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        List<Point> points = new LinkedList<>();

        int retry = Integer.parseInt(br.readLine());

        for (int i = 0; i < retry; i++) {
            String[] input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]);
            int y = Integer.parseInt(input[1]);

            Point point = new Point(x, y);
            points.add(point);
        }

        Collections.sort(points, Collections.reverseOrder());

        for (Point point : points) {
            out.print(point.getX()+" "+point.getY());
            out.println();
        }
        br.close();
    }
}

class Point implements Comparable<Point> {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point o) {
        if (o.x == x && o.y >= y) {
            return 1;
        }
        if (o.x == x && o.y < y) {
            return -1;
        }
        if (o.x > x) {
            return 1;
        }
        return -1;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
