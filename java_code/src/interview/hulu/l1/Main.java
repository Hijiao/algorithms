package l1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static void gen(int[] arr) {
        int[] records = new int[100001];
        int[] rets = new int[arr.length];

        HashMap<Integer, List> map = new HashMap<>();


        for (int i = 0; i < arr.length; i++) {
            int value = arr[i];
            records[value] += 1;
            if (!map.containsKey(value)) {
                ArrayList list = new ArrayList();
                list.add(i);
                map.put(value, list);
            } else {
                map.get(value).add(i);
            }
        }
        int times = 0;
        int total = 0;
        int pre = -1;
        for (int i = 0; i < records.length; i++) {
            times = records[i];
            if (times == 0) {
                continue;
            }
            List<Integer> list = map.get(i);

            for (Integer integer : list) {
                rets[integer] = total;
            }
            total += i * times;
        }


        for (int i = 0; i < rets.length; i++) {
            System.out.println(rets[i]);
        }


    }

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int l = in.nextInt();
        int[] arr = new int[l];
        for (int i = 0; i < l; i++) {
            arr[i] = in.nextInt();
        }
        gen(arr);
    }
}
