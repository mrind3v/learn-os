

public class Adder implements Runnable {
    private Counter counter; 

    Adder(Counter counter){
        this.counter = counter;
    }

    @Override
    public void run(){
        for (int i=0; i<=100; i++){
            counter.increment();
        }
    }
}
