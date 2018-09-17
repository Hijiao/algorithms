package L0047;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class PermutationsII {
    public List<List<Integer>> permuteUnique(int[] nums) {

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
            HashSet usedSet = new HashSet();
            for (int i = 0; i < used.length; i++) {
                if (!used[i] && !usedSet.contains(nums[i])) {
                    used[i] = true;
                    usedSet.add(nums[i]);
                    tmp.add(nums[i]);
                    permute(nums, used, ret, tmp);
                    used[i] = false;
                    tmp.remove(tmp.size() - 1);
                }
            }

        }

    }

    public static void main(String[] args) {
        PermutationsII p = new PermutationsII();
        List<List<Integer>> ret = p.permuteUnique(new int[]{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1});
        System.out.println(ret.toString());
    }
}
