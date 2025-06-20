import java.util.Queue;

public class Producer implements Runnable {
    private String name;
    private int maxSize;
    private Queue<Object> store;  

    public Producer(String name, int maxSize, Queue<Object> store ){
        this.name = name;
        this.maxSize = maxSize; 
        this.store = store; 
    }

    @Override 
    public void run(){

        synchronized(store){ // or Queue.class
            if (store.size() < maxSize){
                System.out.println(this.name + " is producing a shirt " + "and store size: " + store.size());
                store.add(new Object());
            }
        } 

    }

}