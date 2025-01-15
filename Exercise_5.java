import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[l];
        int i = l+1;
        int j = h;
        while(i<=j){
            while(i<=j&&arr[i]<=pivot){
                i++;
            }
            while(i<=j&&arr[j]>pivot){
                j--;
            }
            if(i<=j){
                swap(arr, i, j);
            }
        }
        swap(arr, l, j);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> stack = new Stack<>();

        stack.push(new int[]{l, h});
        while (!stack.isEmpty()) {
            int[] bounds = stack.pop();
            int start = bounds[0];
            int end = bounds[1];

            int pivotIndex = partition(arr, start, end);

            if (pivotIndex - 1 > start) {
                stack.push(new int[]{start, pivotIndex - 1});
            }

            if (pivotIndex + 1 < end) {
                stack.push(new int[]{pivotIndex + 1, end});
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