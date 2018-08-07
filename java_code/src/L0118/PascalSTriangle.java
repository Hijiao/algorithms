package L0118;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class PascalSTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<>(numRows);
        if (numRows == 0) {
            return ret;

        }
        if (numRows >= 1) {
            ret.add(new ArrayList<Integer>(Arrays.asList(1)));
        }
        if (numRows >= 2) {
            ret.add(new ArrayList<Integer>(Arrays.asList(1, 1)));
        }
        if (numRows >= 3) {
            List<Integer> last = ret.get(1);
            for (int row = 3; row <= numRows; row++) {
                List<Integer> curr = new ArrayList<>(row);
                curr.add(1);
                for (int i = 0; i < row - 2; i++) {
                    curr.add(last.get(i) + last.get(i + 1));
                }
                curr.add(1);
                ret.add(curr);
                last = curr;
            }
        }
        return ret;
    }

    public static void main(String[] args) {
        PascalSTriangle ps = new PascalSTriangle();
        List<List<Integer>> ret = ps.generate(1);
        for (List<Integer> l : ret) {
            System.out.println(Arrays.asList(l));
        }
    }

}
