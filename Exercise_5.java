import java.util.ArrayDeque;
import java.util.Deque;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	if (i == j) return;
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	 int pivot = arr[h];
         int i = l;
         for (int j = l; j < h; j++) {
             if (arr[j] <= pivot) {
                 swap(arr, i, j);
                 i++;
             }
         }
         swap(arr, i, h);
         return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    // This avoids recursion by simulating the call stack. Average O(n log n), worst O(n²) like normal quicksort.
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	if (arr == null || arr.length <= 1) return;

        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{0, arr.length - 1});

        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            int lo = range[0], hi = range[1];
            if (lo >= hi) continue;

            int p = partition(arr, lo, hi);

            // Optimization: push larger partition first to keep stack smaller
            int leftSize = (p - 1) - lo;
            int rightSize = hi - (p + 1);

            if (leftSize > rightSize) {
                stack.push(new int[]{lo, p - 1});
                stack.push(new int[]{p + 1, hi});
            } else {
                stack.push(new int[]{p + 1, hi});
                stack.push(new int[]{lo, p - 1});
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
  
   
} 


public class Exercise_5{
	
	 // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.printArr(arr, arr.length); 
        System.out.println("Printed before sorting");
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
}