package leetcode.L0075;

import java.util.Arrays;

public class SortColors {

    public void sortColors(int[] nums) {
        int r = 0, i = 0;
        int b = nums.length - 1;
        while (i <= b) {
            if (nums[i] == 0) {
//                while(nums[r]==0){
//                    r++;
//                }
                if (nums[r] == 0) {
                    i++;
                    r++;
                } else {
                    nums[i] = nums[r];
                    nums[r++] = 0;
                }
            } else if (nums[i] == 2) {
//                while (nums[b]==2){
//                    b--;
//                }
                nums[i] = nums[b];
                nums[b--] = 2;
            } else {
                i++;
            }
        }

        System.out.println(Arrays.toString(nums));
    }

    public static void main(String[] args) {
        SortColors sc = new SortColors();
//        sc.sortColors(new int[]{2, 0, 2, 1, 1, 0});
//        sc.sortColors(new int[]{1,0,2});
        sc.sortColors(new int[]{2,0,1});

    }

}
