package node;

/**
 * Created by Max on 2018/8/18.
 */
public class InterruptExample {
    private  static class Mythrad extends Thread{
        @Override
        public  void run(){
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("not interrupted");
            }

    }

    public static void main(String[] args) throws InterruptedException {

        Mythrad mythrad1 = new Mythrad();

        mythrad1.start();
//        Thread.sleep(2);

//        mythrad1.interrupt();


        System.out.println("main run");
    }

}
