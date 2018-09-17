import java.util.HashMap;

public class L0001TwoSum {

    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                ret[0] = i;
                ret[1] = map.get(target - nums[i]);
            }
            map.put(nums[i], i);
        }
        return ret;
    }

    public static void main(String[] args) {
//        L0001TwoSum t = new L0001TwoSum();
//        System.out.println(Arrays.toString(t.twoSum(new int[]{3,2,4},6)));
        String str = "57 65 20 63 6c 6f 73 65 64 20 6f 75 72 20 24 35 30 4d 20 73 65 72 69 65 73 20 43 20 66 75 6e 64 69 6e 67 2e 20 54 68 61 6e 6b 20 79 6f 75 20 61 6c 6c 2e 20";
        for (String s : str.split(" ")) {
            System.out.print((char) Integer.parseInt(null, 16));
        }
        Integer i = 1;
        i.byteValue();


    }
}
