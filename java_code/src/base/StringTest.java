package base;

/**
 * Created by Max on 2018/8/11.
 */
public class StringTest {

    final static String ffstr1,ffstr2;
    static {
        ffstr1 ="aaa";
        ffstr2 ="bbb";
    }

    /**
     *  1." " 引号创建的字符串在字符串池中
        2.new，new创建字符串时首先查看池中是否有相同值的字符串，如果有，则拷贝一份到堆中，然后返回堆中的地址；如果池中没有，则在堆中创建一份，然后返回堆中的地址（注意，此时不需要从堆中复制到池中，否则导致浪费池的空间）
        3.另外，对字符串进行赋值时，如果右操作数含有一个或一个以上的字符串引用时，则在堆中再建立一个字符串对象，返回引用；如String str2=str1+ "abc";

     * @param args
     */
    public static void main(String[] args) {

        String str1 = "java"; // 指向字符串池
        String str2 = "blog";

        String s4 = "java" + "blog";
        String s5 = "javablog";

        System.out.println("s4 == s5: " + (s4 == s5)); //true

        String s3 = str1 + str2; //编译之后会变成 StringBuffer.append(线程安全、开销更大；没有使用StringBuilder)
        //s是指向堆中值为"javablog"的对象，+运算符会在堆中建立来两个String对象，这两个对象的值分别是"java" "blog".
        //也就是说从字符串池中复制这两个值，然后在堆中创建两个对象，然后再建立对象s,然后将"javablog"的堆地址赋给s.    这句共创建了3个String 对象！

        System.out.println("s4 == s: " + (s4 == s3)); //false
        System.out.println("s3 == \"javablog\": " +(s3 == "javablog ")); //这里返回的false


        final String fstr1 = "java"; // 指向字符串池
        final String fstr2 = "blog";
        String fs = fstr1 + fstr2;
        System.out.println(fs == "javablog"); //这里返回的true  ,因为fstr1和fstr2都为常量，编译时就能确定s的值，所以也放到常量池中


        System.out.println("ffstr1 + ffstr2 == \"aaabbb\": "+(ffstr1 + ffstr2 == "aaabbb"));//这里返回false，因为static代码块在运行时才会初始化


        String fnstr1 = new String("java"); //直接在堆中生成新的“java”
        String fnstr2 = new String("blog");
        String fns = fnstr1 + fnstr2;
        System.out.println(fns == "javablog"); //这里返回的false


    }

}
