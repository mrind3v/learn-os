
public class Counter {
    private int value;

    Counter(int value){
        this.value = value;
    }

    public void increment(){
        value++;
    }

    public void decrement(){
        value--;
    }

    public int getValue(){
        return value;
    }
}