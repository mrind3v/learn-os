import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

public class Client {
    public static void main(String[] args) {
        // every data structure in java has a thread safe version.
        // ConcurrentLinkedQueue is a thread safe queue. It won't allow more than one thread 
        // to act on it at a time. However, we still need to add synchronized keyword in the critical section 
        // because even though the queue is thread safe, it won't prevent threads from reading the condition 
        // that allows them inside the critical section. Only one thread will act at a time, but the other threads will 
        // still be able to read the condition and act on the data structure after the first thread has exited
        // the critical section.
        Queue<Object> store = new ConcurrentLinkedQueue<>(); 
        int maxSize  = 6;
        Producer p1 = new Producer("p1",6,store); 
        Producer p2 = new Producer("p2",6,store); 
        Producer p3 = new Producer("p3",6,store);  

        Consumer c1 = new Consumer(store,"c1");
        Consumer c2 = new Consumer(store,"c2");
        Consumer c3 = new Consumer(store,"c3"); 

        Thread t1 = new Thread(p1);
        Thread t2 = new Thread(p2);
        Thread t3 = new Thread(p3);
        Thread t4 = new Thread(c1);
        Thread t5 = new Thread(c2);
        Thread t6 = new Thread(c3);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
        t6.start();
    }
}