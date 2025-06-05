import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    // public static void main(String[] args) {
    //     for (int i=0; i<100; i++){

    //         // create task which we made in the form of a class 
    //         NumberPrinter np = new NumberPrinter(i);

    //         // create thread and assign task to thread
    //         Thread t = new Thread(np);

    //         // start the thread 
    //         t.start();

    //         // but creating one thread for each no. is not a good idea and
    //         // it will take a lot of time if the numbers to print is huge!
    //         // therefore we use the executor framework
    //     }

    // }


    // the better way
    public static void main(String[] args) {
        ExecutorService ex = Executors.newFixedThreadPool(10);
        
        // or do:
        //ExecutorService ex = Executors.newCachedThreadPool();
        // cached thread pool creates new thread for the task in hand
        // if the existing threads are busy

        // fixed thread pool uses a fixed number of threads. If all threads
        // are busy, new tasks are assigned to thread if one of the fixed
        // number of threads gets freed

        for (int i=0; i<10000; i++){
            NumberPrinter np = new NumberPrinter(i);
            ex.execute(np);
        }

        ex.shutdown(); // otherwise the terminal won't exit
    }
}
