/*Time Complexity:
Best and Average Case: O(n log n)
Worst Case: O(n^2) (if poor pivot is chosen consistently)

Space Complexity:
O(log n) average (stack depth)
O(n) in the worst case */

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = l - 1;

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
        Stack<int[]> stack = new Stack<>();

        // Push initial range
        stack.push(new int[]{l, h});

        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            int low = range[0], high = range[1];

            if (low < high) {
                int pivotIndex = partition(arr, low, high);

                // Push left and right subarray ranges to stack
                if (pivotIndex - 1 > low) {
                    stack.push(new int[]{low, pivotIndex - 1});
                }
                if (pivotIndex + 1 < high) {
                    stack.push(new int[]{pivotIndex + 1, high});
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