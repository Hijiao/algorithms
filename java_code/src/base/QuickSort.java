package base;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by Max on 2018/8/22.
 */
public class QuickSort {

    public static void sort(int[] arr) {
        core(arr, 0, arr.length - 1);
    }

    private static void core(int[] arr, int i, int j) {
        if (i >= j) {
            return;
        }
        int start = i, end = j;
        int baseIndex = ThreadLocalRandom.current().nextInt(i, j);
//        int base = start;

        int baseValue = arr[baseIndex];

        arr[baseIndex] = arr[start];


        while (start < end) {

            while (start < end && arr[end] >= baseValue) {
                end--;
            }
            arr[start] = arr[end];

            while (start < end && arr[start] <= baseValue) {
                start++;
            }
            arr[end] = arr[start];
        }

        arr[start] = baseValue;

        core(arr, i, baseIndex - 1);
        core(arr, baseIndex + 1, j);

    }

    public static void main(String[] args) {
        int[] arr = new int[]{4, 5, 2, 1, 8};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }

}
