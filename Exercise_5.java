import java.lang.reflect.Array;
import java.util.Arrays;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l;

        for(int j=l; j<h; j++) {
            if(arr[j] < pivot) {
                if(i != j)
                    swap(arr, i, j);
                i++;
            }
        }

        if(i != h)
            swap(arr, i, h);

        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack stack = new Stack(h-l+1);

        stack.push(l);
        stack.push(h);

        while(!stack.isEmpty()) {

            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            if(p-1 > l) {
                stack.push(l);
                stack.push(p-1);
            }

            if(p+1 < h) {
                stack.push(p+1);
                stack.push(h);
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
}

class Stack {

    //store the index to the topmost element of the stack
    int top;
    int a[];

    boolean isEmpty()
    {
        //Write your code here
        return top == -1;
    }

    Stack(int size)
    {
        //Initialize your constructor
        top = -1;
        a = new int[size];
    }

    boolean push(int x)
    {
        //Check for stack Overflow
        //Write your code here
        if(top == a.length-1) {
            System.out.println("Stack Overflow");
            return false;
        }

        //Insert data at the top of the stack
        top++;
        a[top] = x;

        return true;
    }

    int pop()
    {
        //If empty return 0 and print " Stack Underflow"
        //Write your code here
        if(isEmpty()) {
            System.out.println("Stack Underflow");
            return 0;
        }

        //Retrieve data from the top of the stack and move pointer 1 index behind
        int ans = peek();
        a[top] = 0;
        top--;

        return ans;
    }

    int peek()
    {
        //Write your code here
        //If empty return -1 and print " Stack is empty"
        if(isEmpty()) {
            System.out.println("Stack is empty");
            return -1;
        }

        //return top most element from the stack
        return a[top];
    }

    void print() {
        System.out.println(Arrays.toString(a));
    }
}