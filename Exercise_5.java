/*TC: O(n ^ 2)
 * SC: O(n) 
 */
import java.util.*;

class Exercise_5 { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if (i != j) {
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
    }
    swap(arr, i + 1, h);
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<>();

        // Push initial values of l and h to stack
        stack.push(l);
        stack.push(h);

        // Keep popping from stack while it's not empty
        while (!stack.isEmpty()) {
            // Pop h and l
            h = stack.pop();
            l = stack.pop();

            // Partition index
            int p = partition(arr, l, h);

            // If elements on left side of pivot, push left side to stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If elements on right side of pivot, push right side to stack
            if (p + 1 < h) {
                stack.push(p + 1);
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
        Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 