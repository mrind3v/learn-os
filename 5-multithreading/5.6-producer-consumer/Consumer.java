import java.util.Queue;

public class Consumer implements Runnable {
    private Queue<Object> store; 
    // private int maxSize; // not used 
    private String name; 

    // public Consumer(Queue<Object> store, int maxSize, String name){
    public Consumer(Queue<Object> store, String name){
        this.store = store; 
        // this.maxSize = maxSize; 
        this.name = name; 
    }

    @Override 
    public void run(){
        synchronized(store){
            if (store.size()>0){
                System.out.println(this.name + " is consuming a shirt " + "and store size: " +store.size());
                store.remove();
            }
        }
    }
}