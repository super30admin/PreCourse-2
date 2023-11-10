import java.io.*;
import java.util.*;
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
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
        int i  = l, j = l;
        while(j < h)
        {
            if(arr[j] <= pivot)
            {
                swap(arr, i++, j);
            }
            j++;
        }
        swap(arr, i, h);
        return i;
        
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty())
        {
            h = stack.pop();
            l = stack.pop();
            if(l >= h) continue;
            int pivot = partition(arr,l, h);
            stack.push(l);
            stack.push(pivot-1);
            stack.push(pivot+1);
            stack.push(h);
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