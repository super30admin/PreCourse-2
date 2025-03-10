class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    arr[i] = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];  // Taking the last element as pivot
        int i = (l - 1); // index of smaller element

        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {  // If current element is smaller than or equal to the pivot
                i++;  // Increment index of smaller element
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h); // Swap pivot to correct position
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];

        // Initialize stack and push initial values of l and h
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;

        // Keep processing elements in the stack
        while (top >= 0) {
            h = stack[top--];  // Pop h
            l = stack[top--];  // Pop l

            // Partition the array
            int p = partition(arr, l, h);

            // Push right side of the partition to the stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }

            // Push left side of the partition to the stack
            if (l < p - 1) {
                stack[++top] = l;
                stack[++top] = p - 1;
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