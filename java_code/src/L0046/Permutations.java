package L0046;

import java.util.ArrayList;
import java.util.List;

public class Permutations {
    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> ret = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        ArrayList tmp = new ArrayList();
        permute(nums, used, ret, tmp);
        return ret;

    }

    private void permute(int[] nums, boolean[] used, List ret, List tmp) {
        if (tmp.size() == nums.length) {
            ret.add(new ArrayList<Integer>(tmp));
        } else {
            for (int i = 0; i < used.length; i++) {
                if (!used[i]) {
                    used[i] = true;
                    tmp.add(nums[i]);
                    permute(nums, used, ret, tmp);
                    used[i] = false;
                    tmp.remove(tmp.size() - 1);
                }
            }

        }

    }

    private void core(int[] nums, int start, List ret) {
        if (start == nums.length) {
            List<Integer> list = new ArrayList<>(nums.length);
            for (int num : nums) {
                list.add(num);
            }
            ret.add(list);
        } else {
            for (int i = start; i < nums.length; ++i) {
                int temp = nums[i];
                nums[i] = nums[start];
                nums[start] = temp;
                core(nums, start + 1, ret);
                temp = nums[i];
                nums[i] = nums[start];
                nums[start] = temp;
            }
        }
    }

    public static void main(String[] args) {
        Permutations p = new Permutations();
        List<List<Integer>> ret = p.permute(new int[]{0, 0, 1, 1});
        System.out.println(ret.toString());
//
//        for(List list:ret){
//            System.out.println(list.toString());
//        }

    }
}
