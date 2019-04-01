package interview.Huawei.L1;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by Max on 2018/8/22.
 */
public class Price {

    private static int choose(int n, double p) {

        double raw_price = p * n;
        double s1 = raw_price;
        if (n >= 3) {
            s1 = raw_price * 0.7;
        }
        if (s1 < 50) {
            s1 += 10;
        }

        double s2 = raw_price;
        s2 = raw_price - s2 / 10 * 2;
        if (s2 < 99) {
            s2 += 6;
        }

        if (s1 == s2) {
            return 0;

        }

        if (s1 < s2) {
            return 1;
        }

        return 2;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double p = sc.nextDouble();
        System.out.println(choose(n, p));
    }
}
