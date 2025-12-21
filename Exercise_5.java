// Time Complexity : Average case - O(n logn), Worst Case - O(n^2) - based on what we choose as pivot
// Space Complexity : In place swapping, 0(1)
// Did this code successfully run on Leetcode :
// Ran into time limit exceeded error
// Any problem you faced while coding this : No
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    {
        int lastIndex = high;
        while (low < high) {
            while(low < high && arr[low] <= arr[lastIndex]){
                low++;
            }

            while(low < high && arr[high] >= arr[lastIndex]){
                high--;
            }
            if(low >= high) break;
            swap(arr, low, high);
        }

        return low;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        // maintain 2 separate stack to capture the current state, that is, lower and higher indices.
        Stack<Integer> lowerIndex = new Stack<>();
        Stack<Integer> endIndex = new Stack<>();

        lowerIndex.push(l);
        endIndex.push(h);

        while(!lowerIndex.isEmpty()){
            int lower = lowerIndex.pop();
            int high  = endIndex.pop();

            int pivot = partition(arr, lower, high);
            swap(arr, pivot, high);

            if(lower < pivot){
                lowerIndex.push(lower);
                endIndex.push(pivot-1);
            }

            if(pivot < high){
                lowerIndex.push(pivot+1);
                endIndex.push(high);
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