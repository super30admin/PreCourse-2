// Time Complexity : worst case: O(n^2), otherwise O(nlogn)
// Space Complexity : worst case: O(n), otherwise O(logn)
// Did this code successfully run on Leetcode : Didn't try on LC
// Any problem you faced while coding this : -


import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if( i != j)
        {
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
        int k = arr[h];
        int i = (l - 1);

        for (int j = l; j < h; j++) {
            if (arr[j] <= k) 
            {
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

        // Push initial values of l and h to the stack
        stack.push(l);
        stack.push(h);

        // Keep popping from the stack while it's not empty
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            int index = partition(arr, l, h);

            if (index - 1 > l) 
            {
                stack.push(l);
                stack.push(index - 1);
            }

            if (index + 1 < h) 
            {
                stack.push(index + 1);
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