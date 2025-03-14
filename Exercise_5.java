class IterativeQuickSort { 
    // Swap two elements without using an extra variable
    void swap(int arr[], int i, int j) { 
        if (i != j) {  // Ensure we don't swap the same element
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function partitions the array and returns the pivot index */
    int partition(int arr[], int l, int h) { 
        int pivot = arr[h];  // Take the last element as pivot
        int i = (l - 1);  // Index of smaller element

        // Loop through the array and compare each element to pivot
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {  // If element is smaller or equal to pivot
                i++;  // Increment index of smaller element
                swap(arr, i, j);  // Swap elements
            }
        }
        
        // Swap pivot element to the correct position
        swap(arr, i + 1, h); 
        return (i + 1);  // Return pivot index
    } 
  
    // Iterative QuickSort using a Stack Data Structure 
    void QuickSort(int arr[], int l, int h) { 
        int[] stack = new int[h - l + 1];  // Stack to hold left and right indexes
        int top = -1;  // Stack pointer

        // Push the initial values of l and h onto the stack
        stack[++top] = l;
        stack[++top] = h;

        // Process the stack until it is empty
        while (top >= 0) { 
            h = stack[top--];  // Pop h
            l = stack[top--];  // Pop l

            // Partition the array and get the pivot index
            int p = partition(arr, l, h);

            // If there's a right subarray, push it to the stack
            if (p + 1 < h) { 
                stack[++top] = p + 1;
                stack[++top] = h;
            }

            // If there's a left subarray, push it to the stack
            if (l < p - 1) { 
                stack[++top] = l;
                stack[++top] = p - 1;
            }
        }
    } 
  
    // A utility function to print the contents of the array 
    void printArr(int arr[], int n) { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();  // New line for better formatting
    } 
  
    // Driver code to test the above 
    public static void main(String args[]) { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1);  
        System.out.println("Sorted array: ");
        ob.printArr(arr, arr.length); 
    } 
}
