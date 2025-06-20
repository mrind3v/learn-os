import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Client {
    public static void main(String[] args) throws InterruptedException{
        Lock lock = new ReentrantLock(); 
        Counter count = new Counter(0);

        Adder add = new Adder(count,lock);
        Subtractor sub = new Subtractor(count,lock);

        Thread t1 = new Thread(add);
        Thread t2 = new Thread(sub);

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("Final value of count is: "+count.getVal());

    }
}
