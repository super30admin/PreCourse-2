import java.util.*;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) { 
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int l = low;
        int r = high-1;
 
        while(true) {
            while(l < high && arr[l] <= pivot) {
                l++;
            }
 
            while(r > 0 && arr[r] >= pivot) {
                r--;
            }
 
            if(l<r) {
                 swap(arr, l, r);
            } else {
                break;
            }
        }
         
         if(l != high) {
             swap(arr, l, high);
         }
 
        return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<SortingTuple> tupleStack = new Stack<>();
        tupleStack.push(new SortingTuple(l, h));

        while(!tupleStack.isEmpty()) {
            SortingTuple peek = tupleStack.pop();
            if(peek.low < peek.high) {
                int index = partition(arr ,peek.low, peek.high);
                tupleStack.push(new SortingTuple(peek.low, index-1));
                tupleStack.push(new SortingTuple(index+1, peek.high));
            }
        }
        //Try using Stack Data Structure to remove recursion.
        
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

    public class SortingTuple {
        int low;
        int high;

        public SortingTuple(int l, int h) {
            this.low = l;
            this.high = h;
        }
    }
} 