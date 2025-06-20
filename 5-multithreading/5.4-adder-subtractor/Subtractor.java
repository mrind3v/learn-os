public class Subtractor implements Runnable {
    private Counter counter; 

    Subtractor(Counter counter){
        this.counter = counter;
    }

    @Override
    public void run(){
        for (int i=0; i<=100; i++){
            counter.decrement();
        }
    }

}
