package interview.neteast.L3;

import java.util.*;

/**
 * Created by Max on 2018/8/11.
 * 字典智能由n个'a' 和m个'z'组成，并按照生序排列，求第k个词是多少。
 */
public class Main {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return ans;
        }
        permute(ans, nums, 0);
        return ans;
    }

    private void permute(List<List<Integer>> ans, int[] nums, int index) {
        if (index == nums.length) {
            List<Integer> temp = new ArrayList<>();
            for (int num : nums) {
                temp.add(num);
            }
            ans.add(temp);
            return;
        }
        Set<Integer> appeared = new HashSet<>();
        for (int i = index; i < nums.length; ++i) {
            if (appeared.add(nums[i])) {
                swap(nums, index, i);
                permute(ans, nums, index + 1);
                swap(nums, index, i);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int save = nums[i];
        nums[i] = nums[j];
        nums[j] = save;
    }

    public void getK(int[] nums, int k) {
        List<List<Integer>> r = permuteUnique(nums);
        if (k > r.size()) {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder();
            List<Integer> ints = r.get(k);
            for (Integer i : ints) {
                sb.append(i == 0 ? 'a' : 'z');
            }
            System.out.println(sb.toString());
        }
    }

    public static void main(String[] args) {
        Main ma = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int[] ins = new int[n + m];
        for (int i = 0; i < m + n; i++) {
            if (i >= n) {
                ins[i] = 1;
            }
        }
        ma.getK(ins, k - 1);
    }
}





