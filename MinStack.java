import java.util.Stack;

public class MinStack {
    Stack<Integer> st;
    Stack<Integer> minSt;
    int min;

    public MinStack(){
       this.st = new Stack<>();
       this.minSt = new Stack<>();
       this.min = Integer.MAX_VALUE;
       minSt.push(Integer.MAX_VALUE);

    }

    public void push(int val){
        min = Math.min(min, val);
        st.push(val);
        minSt.push(min);


    }
    public void pop(){
        st.pop();
        minSt.pop();
        this.min = minSt.peek();

    }

    public int top(){
        return st.peek();
    }

    public int getMin(){
        return min;

    }
    
}
