// Time Complexity : Average : O(nlogn), Worst: O(n^2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

import java.util.*;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = h, start = l;

        for(int i = l; i < pivot; i++) {

            if(arr[i] < arr[pivot]) {
                swap(arr, start, i);
                start++;
            }
        }
        swap(arr, start, pivot);
        return start;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);  

        while(!stack.isEmpty()) {

            h = stack.pop();
            l = stack.pop();

            int pivotIndex = partition(arr, l, h);

            if(pivotIndex - 1 > l) {
                stack.push(l);
                stack.push(pivotIndex - 1);
            }

            if(pivotIndex + l < h) {
                stack.push(pivotIndex + 1);
                stack.push(h);
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