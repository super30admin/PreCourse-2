class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
 
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 
  
    /* This function is same in both iterative and recursive */
    int partition(int arr[], int l, int h) 
    { 
        // Compare elements and swap.
        int pivot = arr[h]; 
        int i = (l - 1); 
        for (int j = l; j < h; j++) { 
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
        // Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1]; 
  
        // initialize top of stack 
        int top = -1; 
  
        // push initial values in the stack 
        stack[++top] = l; 
        stack[++top] = h; 
  
        // keep popping from stack while it's not empty 
        while (top >= 0) { 
            // Pop h and l 
            h = stack[top--]; 
            l = stack[top--]; 
  
            // Set pivot element at its correct position 
            int p = partition(arr, l, h); 
  
            // If there are elements on the left of pivot, push them to stack 
            if (p - 1 > l) { 
                stack[++top] = l; 
                stack[++top] = p - 1; 
            } 
  
            // If there are elements on the right of pivot, push them to stack 
            if (p + 1 < h) { 
                stack[++top] = p + 1; 
                stack[++top] = h; 
            } 
        } 
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();
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
