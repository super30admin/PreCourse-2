// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : 
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;
        for(int j = l; j <= h - 1; j++){
            if(arr[j] <= pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;

        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSortIterative(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
  
        // initialize top of stack
        int top = -1;
  
        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;
  
        // Keep popping from stack while is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];
  
            // Set pivot element at its correct position
            // in sorted array
            int p = partition(arr, l, h);
  
            // If there are elements on left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }
  
            // If there are elements on right side of pivot,
            // then push right side to stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
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
        ob.QuickSortIterative(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 