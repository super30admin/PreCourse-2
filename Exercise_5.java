// Time Complexity : O(n * log n) in average case, O(n^2) in worst case
// Space Complexity : O(log n) due to the stack used for iterative calls
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


class IterativeQuickSort { 
    void swap(int arr[], int i, int j) {
        // Swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and recursive */
    int partition(int arr[], int l, int h) { 
        int pivot = arr[h];
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) { 
        // Create an auxiliary stack
        int[] stack = new int[h - l + 1];
        int top = -1;

        // Push initial values to stack
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            // Pop h and l
            h = stack[top--];
            l = stack[top--];

            // Partition the array and get the pivot
            int p = partition(arr, l, h);

            // If there are elements on the left side of pivot, push them to stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If there are elements on the right side of pivot, push them to stack
            if (p + 1 < h) {
                stack[++top] = p + 1;
                stack[++top] = h;
            }
        }
    } 
  
    // A utility function to print contents of array
    void printArr(int arr[], int n) { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();
    } 
  
    // Driver code to test above 
    public static void main(String args[]) { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 
