import java.util.Stack;

// Time Complexity : Need to refresh my knowledge on this.
// Space Complexity : Need to refresh my knowledge on this.
// Did this code successfully run on Leetcode : YES(Over local ide).
// Any problem you faced while coding this : Took time to understand and still couldn't understand properly (its just i remember from youtube how to do it.) AND t.c and s.c.

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        if (i!=j) { // because of duplicate values.
            //Try swapping without extra variable : Example -> i = 5 , j= 10.
            arr[i] = arr[i] + arr[j]; //i = 5+10 = 15
            arr[j] = arr[i] - arr[j];//arr[j] = 15 - 10 = 5
            arr[i] = arr[i] - arr[j]; //arr[i] = 15-5 = 10
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    { 
        //Compare elements and swap.
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int iIndex = low-1;
        for(int j = low; j < high; j++){
            if(arr[j] <= pivot){
                iIndex++;
                swap(arr,iIndex,j);
            }
        }
        swap(arr,iIndex+1,high);
        return iIndex+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack<int[]> stack = new Stack<int[]>();
        stack.push(new int[] {l,h});
        while (!stack.empty())
        {
            int[] range = stack.pop();
            int low= range[0];
            int high = range[1];

            int pivot = partition(arr,low,high);

            if (pivot-1 >low)
            {
                stack.push(new int[] {low, pivot-1});
            }
            if (pivot+1 < high)
            {
                stack.push(new int[] {pivot+1, high});
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