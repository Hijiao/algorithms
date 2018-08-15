package interview.neteast.L1;

/**
 * Created by Max on 2018/8/11.
 */

import java.util.Scanner;

/**
 * 上课收益为 points[] ,是否清清醒为 wakes[] ，叫醒一次可清醒k分钟，求叫醒一次的最大收益。
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        if (n == 0) {
            System.out.println(0);
        }

        int[] points = new int[n];
        int[] wakes = new int[n];

        for (int i = 0; i < n; i++) {
            points[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            wakes[i] = sc.nextInt();
        }


//        System.out.println(Arrays.toString(inters));
//        System.out.println(Arrays.toString(wakes));

        System.out.println(core(points, wakes, n, k));

    }

    private static int core(int[] points, int[] wakes, int n, int k) {


        int base = 0;
        for (int i = 0; i < n; i++) {
            if (wakes[i] == 1) {
                base += points[i];
            }
        }

        int total_add_k = 0;
        int max_k = 0;
        for (int i = 0; i < n; i++) {
            if (i < k) {
                if (wakes[i] == 0) {
                    total_add_k += points[i];
                }
            } else {
                if (wakes[i] == 0) {
                    total_add_k += points[i];
                }
                if (wakes[i - k] == 0) {
                    total_add_k -= points[i - k];
                }
            }
            max_k = Math.max(total_add_k, max_k);
        }

        return base + max_k;

    }

}