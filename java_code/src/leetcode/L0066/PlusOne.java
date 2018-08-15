package leetcode.L0066;

import java.util.Arrays;
import java.util.LinkedList;

public class PlusOne {

    public int[] plusOne(int[] digits) {
        LinkedList<Integer> list = new LinkedList<Integer>();

        int carry = 1;

        for (int i = digits.length - 1; i >= 0; i--) {
            int t = carry + digits[i];
            if (t == 10) {
                list.addFirst(0);
                carry = 1;
            } else {
                list.addFirst(t);
                carry = 0;
            }
        }
        if (carry == 1) {
            list.addFirst(1);
        }
        int[] ret = new int[list.size()];
        int index = 0;
        for (Integer i : list) {
            ret[index++] = i;
        }
        return ret;
    }

    public static void main(String[] args) {
        PlusOne po = new PlusOne();
        System.out.println(Arrays.toString(po.plusOne(new int[]{0})));
    }
}
