package interview.neteast.L2;

import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * Created by Max on 2018/8/11.
 * 一共有n个堆，每堆容量为 heaps[] ，回答m个问题，即第qs[i]苹果在第几堆。
 */

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] heaps = new int[n];

        for (int i = 0; i < n; i++) {
            heaps[i] = sc.nextInt();
        }
        int m = sc.nextInt();
        int[] qs = new int[m];
        for (int i = 0; i < m; i++) {
            qs[i] = sc.nextInt();
        }

//        System.out.println(Arrays.toString(heaps));
//        System.out.println(Arrays.toString(qs));
        core(heaps, qs, n, m);

//        System.out.println(core(inters, wakes, n, k));

    }

    private static void core(int[] heaps, int[] qs, int n, int m) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int t = 0;

        for (int i = 0; i < n; i++) {
            t += heaps[i];
            map.put(t, i + 1);
        }
        for (int i = 0; i < m; i++) {
            Map.Entry<Integer, Integer> e = map.ceilingEntry(qs[i]);
            System.out.println(e.getValue());
        }

    }
}
