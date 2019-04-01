package interview.Huawei.L1;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

/**
 * Created by Max on 2018/8/22.
 */
public class FindLongestDNA {

    private String str;

    private void findLongest(String s) {

        for (int k = s.length() - 1; k > 0; k--) {
            HashSet<String> hashSet = new HashSet();
            for (int i = 0; i <= s.length() - k; i++) {
                String x = s.substring(i, i + k);
                if (hashSet.contains(x)) {
                    str = x;
                    return;
                } else
                    hashSet.add(x);
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
//        if(args.length > 1)
//            System.setIn(new FileInputStream(args[1]));
        Scanner sc = new Scanner(System.in);
        FindLongestDNA m = new FindLongestDNA();
        String str = sc.next();
        m.findLongest(str);
        if (m.str == null) {
            System.out.println(" 0");
        } else
            System.out.println(m.str + " " + m.str.length());
    }
}
