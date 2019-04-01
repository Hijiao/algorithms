package base;

/**
 * Created by Max on 2018/8/22.
 */
public class BinSelect {

    public static int binSelectLeft(int arr[], int t) {
        int lo = 0, hi = arr.length - 1, i = 0;

        while (lo < hi) {
            i = (lo + hi) >> 1;
            if (arr[i] < t) {
                lo = i + 1;
            } else hi = i;
        }
        return lo;
    }

    public static void main(String[] args) {
        System.out.println(binSelectLeft(new int[]{2, 4, 5, 5, 5, 5, 5, 5, 7, 8}, 6));
    }
}
