// Time Complexity : O(NlogN)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : No, did not find it on Leetcode.
// Any problem you faced while coding this : No, working on recursive approach first helped.
import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if (i == j || arr[i] == arr[j]) {
            // The value of XOR of two same numbers will be 0.
            return;
        }
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j]; // = (arr[i] ^ arr[j]) ^ arr[j] = arr[i]
        arr[i] = arr[i] ^ arr[j]; // = (arr[i] ^ arr[j]) ^ arr[i] = arr[j]
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        // Taking the last element as pivot.
        int pivot = arr[h]; 
        int i = l - 1;
        // Place all elements less than pivot on the left side of the array.
        for (int j = l; j < h; j ++) { 
            if (arr[j] <= pivot) {
                i ++;
                swap(arr, i, j);
            }
        }
        // Place pivot in the partition index,
        // where all elements on the left are less than pivot
        // and all elements on the right are greater than the pivot.
        swap(arr, i + 1, h);
        // Return pivot index.
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            h = stack.pop(); // h index will be popped first
            l = stack.pop();
            if (l < h) {
                int pivotIndex = partition(arr, l, h);
                if (pivotIndex - 1 > l) {
                    // Consider the left subarray and push the indices to the stack.
                    stack.push(l);
                    stack.push(pivotIndex - 1);    
                }
                if (pivotIndex + 1 < h) {
                    // Consider the right subarray and push the indices to the stack.
                    stack.push(pivotIndex + 1);
                    stack.push(h);
                }
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