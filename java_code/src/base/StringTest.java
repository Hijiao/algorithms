package base;

/**
 * Created by Max on 2018/8/11.
 */
public class StringTest {

    public static void main(String[] args) {

        String str1 = "java"; // 指向字符串池
        String str2 = "blog";
        String s = str1 + str2;
        System.out.println(s == "javablog"); //这里返回的false


        final String fstr1 = "java"; // 指向字符串池
        String fstr2 = "blog";
        String fs = fstr1 + fstr2;
        System.out.println(fs == "javablog"); //这里返回的true

        final String fnstr1 = new String("java"); // 指向字符串池
        final String fnstr2 = new String("blog");
        final String fns = fnstr1 + fnstr2;
        System.out.println(fns == "javablog"); //这里返回的false


    }

}
