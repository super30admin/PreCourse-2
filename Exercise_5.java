import java.util.Stack;
// Time Complexity : O(n^2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes - Used IntelliJ
// Any problem you faced while coding this : I was not aware of the concept before, so went through it

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    {
        //Write code here for Partition and Swap
        int pivot = arr[high];
        int j = low - 1;
        for(int i =low;i<=high-1;i++) {
            if(arr[i] <= pivot) {
                j++;
                swap(arr,i,j);
            }
        }
        arr[high] = arr[j+1];
        arr[j+1] = pivot;
        return j+1;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            int p = partition(arr, l, h);
            if(p-1 > l) {
                stack.push(l);
                stack.push(p-1);
            }
            if(p+1 < h) {
                stack.push(l);
                stack.push(p+1);
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