import java.util.concurrent.locks.Lock; // contains the mutex lock

public class Adder implements Runnable{
    private Counter count;
    private Lock lock; // no need if you use synchronized(count)

    Adder(Counter count, Lock lock){
        this.count = count;
        this.lock = lock; // no need if you use synchronized(count)
    }

    @Override
    public void run(){
        synchronized(count){
            //lock.lock();
            for (int i=0; i<=100; i++){
                count.increment();
            }
            //lock.unlock();
        }
    }
}
