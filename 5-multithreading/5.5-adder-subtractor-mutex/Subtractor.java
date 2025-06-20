import java.util.concurrent.locks.Lock;

public class Subtractor implements Runnable {
    private Counter count; 
    private Lock lock; // no need if you use synchronized(count)

    Subtractor(Counter count, Lock lock){
        this.count = count; 
        this.lock = lock; // no need if you use synchronized(count)
    }

    @Override 
    public void run(){
        // or do synchronized(Counter.class) to protect the whole class (all instances of the class)
        synchronized(count){
            //lock.lock();
            for (int i=0; i<=100; i++){
                count.decrement();
            }
            //lock.unlock();
        }
    }
}
