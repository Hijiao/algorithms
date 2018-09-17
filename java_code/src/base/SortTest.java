package base;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class SortTest {
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        quickSortCore(arr, 0, arr.length - 1);
    }

    public static void quickSortCore(int[] arr, int start, int end) {
        if (end <= start) {
            return;
        }
        int i = start, j = end;

        int baseIndex = ThreadLocalRandom.current().nextInt(i, j);
        int base = arr[baseIndex];

        arr[baseIndex] = arr[i];
        while (i < j) {
            while (i < j && arr[j] >= base) {
                j--;
            }
            arr[i] = arr[j];

            while (i < j && arr[i] < base) {
                i++;
            }
            arr[j] = arr[i];
        }
        arr[i] = base;

        quickSortCore(arr, start, i - 1);
        quickSortCore(arr, i + 1, end);

    }

    public static void main(String[] args) {
        int[] l = {1, 2, 34, 6, 0};

        quickSort(l);
        System.out.println(Arrays.toString(l));
    }

}
