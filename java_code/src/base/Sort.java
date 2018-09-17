package base;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Sort {

    private static void quickSortCore(int[] arr, int i, int j) {
        int start = i, end = j;
        if (start >= end) {
            return;
        }
        int baseIndex = ThreadLocalRandom.current().nextInt(start, end);
//        int baseIndex = 3;

        int base = arr[baseIndex];
        arr[baseIndex] = arr[start];
//        int tmp = arr[start];
        int temp;
        while (start < end) {
            while (arr[end] >= base) {
                end--;
            }
            while (arr[start] <= base) {
                start++;
            }
            if (start < end) {
                temp = arr[start];
                arr[start] = arr[end];
                arr[end] = temp;
                start++;
                end--;
            }
        }
        arr[start] = base;
        quickSortCore(arr, i, start - 1);
        quickSortCore(arr, start + 1, j);

    }


    public static void quickSort(int[] arr) {
        if (arr == null || arr.length == 0)
            return;

        quickSortCore(arr, 0, arr.length - 1);
    }

    public static void main(String[] args) {
//        int[] arr = new int[]{1, 3, 41, 24, 45, 43, 7, 1, 3, 46, 4};
        int[] arr = {3, 1, 1, 3, 1, 1, 1, 3};
        Arrays.sort(args);
        Sort.quickSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
