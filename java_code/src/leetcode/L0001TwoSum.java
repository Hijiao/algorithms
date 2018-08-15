package leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class L0001TwoSum {

    public int[] twoSum(int [] nums, int target){
        int [] ret = new int[2];
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>(nums.length);
        for(int i = 0; i < nums.length; i++){
            if (map.containsKey(target - nums[i])) {
                ret[0]= i;
                ret[1] = map.get(target - nums[i]);
            }
            map.put(nums[i],i);
        }
        return ret;
    }

    public static void main(String[] args) {
        L0001TwoSum t = new L0001TwoSum();
        System.out.println(Arrays.toString(t.twoSum(new int[]{3,2,4},6)));
    }
}
