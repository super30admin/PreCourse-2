// Time Complexity :O(n*log(n))
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :I am not able to get the output without using an extra element wile swapping

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        //Try swapping without extra variable 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int low=l,high=h;
        //Compare elements and swap.
        int pivot = arr[high];
        int i = low - 1;
 
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
            i++;
            swap(arr, i, j);
            }
        }
 
        swap(arr, i + 1, high);
        
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int low=l,high=h;
        //Try using Stack Data Structure to remove recursion.
        // Create an auxiliary stack
        int[] stack = new int[high - low + 1];
        
        // initialize top of stack
        int top = -1;
        
        // push initial values of low and high to stack
        stack[++top] = low;
        stack[++top] = high;
        
        // Keep popping from stack while is not empty
        while (top >= 0) {
            // Pop high and low
            high = stack[top--];
            low = stack[top--];
        
            // Set pivot element at its correct position in sorted array
            int p = partition(arr, low, high);
        
            // If there are elements on left side of pivot, then push left
            // side to stack
            if (p - 1 > low) {
            stack[++top] = low;
            stack[++top] = p - 1;
            }
        
            // If there are elements on right side of pivot, then push right
            // side to stack
            if (p + 1 < high) {
            stack[++top] = p + 1;
            stack[++top] = high;
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