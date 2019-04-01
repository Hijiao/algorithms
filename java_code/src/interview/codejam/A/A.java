package A;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class A {

    private static int consume(int[] cups, int K) {

        Arrays.sort(cups);
        int total = 0;
        int currday = 1;
        int rk = K;
        for (int i = 0; i < cups.length; i++) {
            if (cups[i] >= currday) {
                if (rk > 1) {
                    rk--;
                    total++;
                } else if (rk == 1) {
                    rk = K;
                    currday++;
                    total++;
                }
            }
        }
        return total;
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();
        for (int i = 1; i <= t; i++) {
            int n = in.nextInt();
            int k = in.nextInt();
            int[] cups = new int[n];
            for (int j = 0; j < n; j++) {
                cups[j] = in.nextInt();
            }
            System.out.println("Case #" + i + ": " + consume(cups, k));
        }

//        System.out.println(consume(new int[]{2, 2,}, 1));

    }
}
