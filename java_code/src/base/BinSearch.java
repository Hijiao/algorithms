package base;

public class BinSearch {

    //如果存在，返回任意位置，不分左右。若不存在，返回应该插入的下表
    public static int binsearch(int[] arr, int target) {
        int end = arr.length;
        int start = 0;
        int base = -1;
        while (start < end) {
            base = (start + end) >> 1;
            if (arr[base] < target) {
                start = base + 1;
            } else if (arr[base] > target) {
                end = base - 1;
            } else break;
        }
        return base;
    }

    //如果存在，返回最右的index，否则返回插入的坐标，注意，如果插在最后，index会溢出
    public static int binSearchRight(int[] arr, int t) {
        int start = 0;
        int end = arr.length;
        int base;

        while (start < end) {
            base = (start + end) >> 1;
            if (arr[base] > t) {
                end = base - 1;
            } else {
                start = base + 1;
            }
        }
        if (arr[start] == t) {
            return start;
        }
        return -1;
    }


    //如果存在，返回最左的index，否则返回插入的坐标
    public static int binSearchLeft(int[] arr, int t) {
        int start = 0;
        int end = arr.length;

        int base;
        while (start < end) {
            base = (start + end) >> 1;
            if (arr[base] < t) {
                start = base + 1;
            } else {
                end = base;
            }
        }
        return start;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{0, 2, 3};
        System.out.println(binsearch(arr, 3));
    }

}
