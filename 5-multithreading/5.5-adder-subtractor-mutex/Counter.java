public class Counter {
    private int val;

    Counter(int val){
        this.val=val;
    }

    public void increment(){
        val++;
    }

    public void decrement(){
        val--;
    }

    public int getVal(){
        return val;
    }
}
