package leetcode.L0119;

import java.util.ArrayList;
import java.util.List;

public class PascalSTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ret = new ArrayList<>(rowIndex + 1);
        for (int row = 0; row <= rowIndex; row++) {
            ret.add(1);
            for (int i = row - 1; i > 0; i--) {
                ret.set(i, ret.get(i) + ret.get(i - 1));
            }
        }

        return ret;
    }

    public static void main(String[] args) {
        PascalSTriangleII ps = new PascalSTriangleII();
        List<Integer> l = ps.getRow(3);
        System.out.println(l.toString());
    }
}
