// Time Complexity : O(N^2) 
// Space Complexity : O(logN) 
// Did this code successfully run on Leetcode : Yes 
// Any problem you faced while coding this:  No
// Your code here along with comments explaining your approach: In this method we use stack for implementing the recursive approach. We push the low and high from array into the stack and the pop the indices. Then, we perform the partition and push new subarray indices onto the stack until it's empty.

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if (i != j) {
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot=arr[l];
        int i=l;
        for(int j=l+1;j<=h;j++)
        {
            if(arr[j]<pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, l, i);
        return i;

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack=new Stack<>();
        stack.push(l);
        stack.push(h);

        while(!stack.isEmpty())
        {
             h=stack.pop();
             l=stack.pop();
             
        int pindex=partition(arr, l, h);

        if (pindex-1>l)
        {
        stack.push(l);
        stack.push(pindex-1);
        }
        
        if (pindex-1>l)
        {
        stack.push(h);
        stack.push(pindex+1);
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