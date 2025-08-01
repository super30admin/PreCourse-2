// Time Complexity : O(nlogn) avg case O(n^2) worst case
// Space Complexity : O(logn) stack space
import java.util.Stack;
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
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l;
        for(int j = l; j < h; j++){
            if(arr[j] < pivot){
                swap(arr, i, j);
                i++;
            }
        }
        swap(arr, i, h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> s = new Stack<>();
        s.push(new int[]{l, h});

        while(!s.isEmpty()){
            int[] range = s.pop();
            int start = range[0];
            int end = range[1];

            if(start < end){
                // get new pivot
                int pivot = partition(arr, start, end);
                // put new range for left
                s.push(new int[]{start, pivot - 1});
                // put new range for right
                s.push(new int[]{pivot + 1, end});
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
        int arr[] = { 9, 8, 7, 6, 5, 4, 3, 2, 1 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 