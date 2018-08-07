package L0867;

import java.util.Arrays;

public class TransposeMatrix {
    public int[][] transpose(int[][] A) {
        int[][] ret = new int[A[0].length][A.length];

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {

                ret[j][i] = A[i][j];
            }

        }
        return ret;
    }

    public static void main(String[] args) {
        int[][] A = {{1, 2, 3}, {4, 5, 6}};
        int[][] B = new TransposeMatrix().transpose(A);
        for (int[] b : B) {
            System.out.println(Arrays.toString(b));
        }
    }
}
