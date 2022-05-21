import java.util.Stack;

class IterativeQuickSort {
    // Time Complexity : O(nlogn)
    // Space Complexity : O(n) n elements in an array
    // Any problem you faced while coding this : Couldn't figure out how stack will help in this.
    void swap(int[] arr, int i, int j)
    { 
	//Try swapping without extra variable
        arr[i] = arr[i]+arr[j];
        arr[j] = arr[i]-arr[j];
        arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int l, int h)
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l-1;
        for (int j=l;j<h;j++){
            if(arr[j] <= pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);

        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        //Not sure what to do next;
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String[] args)
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 