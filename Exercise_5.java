// Time Complexity : O(n2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : struggled while implementing swap.
// I was getting error when i=j, I had to print everything to fing the error;
// Your code here along with comments explaining your approach
// choose one pivot element, put all the small element of array on left side of pivot and large element on right side.
// then sort left and right side.

import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i != j){
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
        // int temp = arr[i];
        // arr[i] = arr[j];
        // arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];  
        int i = (l-1); 
        for (int j=l; j<h; j++) 
        { 
            if (arr[j] <= pivot) 
            { 
                i++; 
                swap(arr,i,j);
            } 
        } 
        swap(arr,i+1,h);
  
        return i+1; 
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l); 
        stack.push(h); 
        while (!stack.isEmpty()) { 
            h = stack.pop(); 
            l = stack.pop(); 
            int index = partition(arr, l, h); 
            if (index - 1 > l) { 
                stack.push(l); 
                stack.push(index - 1); 
            } 
            if (index + 1 < h) { 
                stack.push(index + 1); 
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