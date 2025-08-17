import java.util.Stack;

// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Unable to get swap to work without tmp. See commented code for attempt
class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

//        arr[i] = arr[i] + arr[j];
//        arr[j] = arr[i] - arr[j];
//        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int i = (l - 1);
        for (int j = l; j <= h-1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) {
        Stack<Integer> s = new Stack<>();
        s.push(0);
        s.push(arr.length - 1);

        while (!s.isEmpty()) {
            int end = s.pop();
            int start = s.pop();

            if (start >= end) {
                continue;
            }

            int pivot = partition(arr, start, end);
            if (pivot + 1 < end) {
                s.push(pivot + 1);
                s.push(end);
            }

            if (start < pivot - 1) {
                s.push(start);
                s.push(pivot - 1);
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