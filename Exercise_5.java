// Time Complexity : O(n log n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : Yes

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;

        for (int j = l; j < h; ++j) {
            //  If current element is smaller than pivot, then swap
            if (arr[j] < pivot) {
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
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();

        stack.push(l);
        stack.push(h);

        while (!stack.empty()) {
            h = stack.pop();
            l = stack.pop();

            //  Setting pivot element to its correct position
            int pos = partition(arr, l, h);

            // Elements on the left side of the pivot are pushed into the stack if present
            if (pos -1 > l) {
                stack.push(l);
                stack.push(pos - 1);
            }

            // Elements on the right side of the pivot are pushed into the stack if present
            if (pos + 1 < h) {
                stack.push(pos + 1);
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