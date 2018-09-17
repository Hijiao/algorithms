package L0220;

import java.util.TreeSet;

public class ContainsDuplicateIII {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0 || k <= 0) {
            return false;
        }

        final TreeSet<Long> values = new TreeSet<>();
        for (int ind = 0; ind < nums.length; ind++) {

            final Long floor = values.floor(((long) nums[ind] + t));
            final Long ceil = values.ceiling(((long) nums[ind] - t));
            if ((floor != null && floor >= nums[ind])
                    || (ceil != null && ceil <= nums[ind])) {
                return true;
            }

            values.add((long) nums[ind]);
            if (ind >= k) {
                values.remove((long) nums[ind - k]);
            }
        }

        return false;
    }
//        HashMap<Integer,Integer> map = new HashMap<>();
//        for (int i = 0;i< nums.length;i++){
//            for (int d = i-k; d!= i&&d<=i+k;d++ ){
//                if (map.getOrDefault(d,Integer.MAX_VALUE) - i <=t){
//                    return true;
//                }
//                map.put()
//            }
//        }

//        for (int i = 0; i < nums.length; i++) {
//            for (int s = Math.max(0, i - k); s < i; s++) {
//                if (Math.abs((float)nums[i] - nums[s]) <= t) {
//                    return true;
//                }
//            }
//        }
//        return false;
//    }

    public static void main(String[] args) {
        ContainsDuplicateIII cd = new ContainsDuplicateIII();
        System.out.println(cd.containsNearbyAlmostDuplicate(new int[]{1, 5, 9, 1, 5, 9}, 2, 3));
        System.out.println(Math.abs((float) -1 - Integer.MAX_VALUE));
    }
}
