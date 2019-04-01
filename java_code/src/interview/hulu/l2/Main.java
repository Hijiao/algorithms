package l2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private class Node implements Comparable<Node> {
        HashSet<Node> parents = new HashSet<>();
        HashSet<Node> childrens = new HashSet<>();

        Integer id;

        Node(Integer id) {

            this.id = id;
        }

        void setSon(Node son) {
            this.childrens.add(son);
        }

        void setParents(Node p) {
            this.parents.add(p);
        }

//        @Override
//        public int compare(Node o1, Node o2) {
//            return o1.id-o2.id;
//        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return Objects.equals(id, node.id);
        }

        @Override
        public int hashCode() {
            return Objects.hash(id);
        }


        @Override
        public int compareTo(Node o) {
            return id - o.id;
        }
    }

    HashMap<Integer, Node> nodes = new HashMap<>();

    TreeSet<Node> noSons = new TreeSet<>();

    private int totalNode = 0;

    private void buildShip(Integer id, Integer son) {
//        System.out.println("build " + id + " " + son);
        Node curr = nodes.get(id);

        if (curr == null) {
            curr = new Node(id);
            nodes.put(id, curr);
            totalNode++;
        } else noSons.remove(curr);

        Node sonNode = nodes.get(son);
        if (sonNode == null) {
            sonNode = new Node(son);
            noSons.add(sonNode);
            totalNode++;
            nodes.put(son, sonNode);

        }

        curr.setSon(sonNode);

        sonNode.setParents(curr);

    }

    private void fill(int m) {

        for (int i = 1; i <= m; i++) {
            if (nodes.containsKey(i)) {
                continue;
            } else {
                Node n = new Node(i);
                nodes.put(i, n);
                noSons.add(n);
            }
        }

    }

    private void doneOne(Node node, HashSet<Node> newNoSon) {
        for (Node p : node.parents) {
            if (p.childrens.size() <= 1) {
                newNoSon.add(p);
            } else {
                p.childrens.remove(node);
            }

        }
//        System.out.println("done one");

    }

    private void consume(int maxC, int m) {
        int day = 0;
        int finiesh = 0;
        HashSet<Node> newNoSon = new HashSet<>(maxC);
        while (!noSons.isEmpty()) {
            newNoSon.clear();
            int i = 0;
            day += 1;
            Iterator iterator = noSons.iterator();

            while (iterator.hasNext() && i++ < maxC) {
                finiesh += 1;
                Node todone = (Node) iterator.next();
                System.out.println(todone.id
                );

                doneOne(todone, newNoSon);
                iterator.remove();
            }
            noSons.addAll(newNoSon);
//            for (Node node : noSons) {
//                if (i++ < maxC) {
//                    doneOne(node);
//                } else {
//                    break;
//                }
//            }

        }
//        System.out.println( "f m" + finiesh +" " + m);
        if (finiesh < m) {
            System.out.println("E");
        } else System.out.println(day);


    }

    public static void main(String[] args) {
        Main ma = new Main();
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int m = in.nextInt();
        int n = in.nextInt();
        int k = in.nextInt();

        for (int i = 0; i < k; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            ma.buildShip(a, b);
        }
        ma.fill(m);
        ma.consume(n, m);
    }
    /**
     6 2 5
     2 1
     3 1
     5 2
     5 3
     6 5
     **/
}
