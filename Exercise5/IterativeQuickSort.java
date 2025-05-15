package Exercise5;
import java.util.*;
// Time Complexity : average- O(n log n), worst - O(n^2)
// Space Complexity : O(n)
// Any problem you faced while coding this : No

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
	    //swapping without extra variable using xor
        if(i != j) {
            arr[i] ^= arr[j];
            arr[j] ^= arr[i];
            arr[i] ^= arr[j];
        }
    } 

    int partition(int arr[], int low, int high)
    { 
        //Compare elements and swap.
        int pivot = arr[high];
        int i = low - 1;
        for(int j = low; j < high; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        i++;
        swap(arr, i, high);
        return i; // new pivot
    } 


    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stk = new Stack<>();
        stk.push(h);
        stk.push(l);

        while(!stk.isEmpty()) {
            int low = stk.pop();
            int high = stk.pop();

            int pivot = partition(arr, low, high);

            if(low < pivot - 1) {
                stk.push(pivot -1);
                stk.push(low);
            }
            if(pivot + 1 < high) {
                stk.push(high);
                stk.push(pivot+1);
            }
        }

    } 

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