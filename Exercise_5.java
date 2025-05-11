//Time complexity: best+average case: O(nlogn) worst case: O(n^2)
//Space complexity: best+average case: O(logn) worst case: O(n) //for stack
import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        //Try swapping without extra variable
        if(i!=j){
            arr[i] = arr[i]+arr[j];
            arr[j] = arr[i]-arr[j];
            arr[i] = arr[i]-arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
        //Write code here for Partition and Swap 
        if(high==low){
            return low;
        }
        int pivot = arr[high], pivotIndex = high;
        int i = low, j = high-1;
        while(i<=j){
            while(i<=high-1 && arr[i]<=pivot){
                i++;
            }
            while(j>=low && arr[j]>=pivot){
                j--;
            }
            if(i<j){
                swap(arr, i,j);
            }
        }
        swap(arr, pivotIndex, j+1);
        return j+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while(!stack.empty()){
            int high = stack.pop();
            int low = stack.pop();
            int part = partition(arr, low, high);
            if(part!=low){
                stack.push(low);
                stack.push(part-1);
                QuickSort(arr, low, part-1);
            }
            if(part!=high){
                stack.push(part+1);
                stack.push(high);
                QuickSort(arr, part+1, high);
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
        //int arr[] = { 9, 8, 7, 6, 5, 4, 3, 2, 1};
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 