package L0071;


import java.util.LinkedList;

public class SimplifyPath {
    private int index = 0;
    private String p;

    private String nextToken() {

        while ((index < p.length()) && p.charAt(index) == '/') {
            index++;
        }
        int start = index;
        while ((index < p.length()) && p.charAt(index) != '/') {
            index++;
        }
        return p.substring(start, index);
    }


    public String simplifyPath(String path) {
        if (path == null || path.isEmpty()) {
            return "";
        }
        boolean startWithSlash = false;
        if (path.charAt(0) == '/') {
            startWithSlash = true;
        }
        this.p = path;
        String token;
        LinkedList<String> queue = new LinkedList<>();

        while (!(token = nextToken()).equals("")) {
            if ("..".equals(token)) {
                queue.pollLast();
            } else if (".".equals(token)) {
                continue;
            } else {
                queue.addLast(token);
            }
        }

        String ret = String.join("/", queue);

        if (startWithSlash) {
            ret = "/" + ret;
        }
        return ret;
    }

    public static void main(String[] args) {
        SimplifyPath s = new SimplifyPath();
        System.out.println(s.simplifyPath("////TJbrd/owxdG////"));
    }

}
