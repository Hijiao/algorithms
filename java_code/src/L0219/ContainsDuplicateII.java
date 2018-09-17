package L0219;

import java.util.HashMap;

public class ContainsDuplicateII {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {

            if (map.containsKey(nums[i]) && (i - map.get(nums[i]) <= k)) {
                return true;
            }
            map.put(nums[i], i);
        }
        return false;
    }

    public static void main(String[] args) {
        ContainsDuplicateII cd = new ContainsDuplicateII();
        System.out.println(cd.containsNearbyDuplicate(new int[]{1, 2, 3, 1, 2, 3}, 4));
    }
}