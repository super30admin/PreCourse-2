// Time Complexity : O (n log n)
// Space Complexity : O (log n)
// Did this code successfully run on Leetcode : Ran it on VS Code. 
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
// Find the partition index for the given array. Add the left and right part of partition into stack as 
// [lower,partition-1] and [partition+1,high]. Check if stack has any elements. Take the top element and
// and find the partition index for the array with range based on popped element, then add two resultant 
// arrays in the stack and continue the process until stack has no elements. Make sure the left < pivot -1 
// before adding it to the stack and also check that pivot+1 < right before adding to the stack.  
// To find the partition index of a given array start with last element as pivot. Take two pointers i and j 
// that start from index 0 and check if value at index i in array is less than or equal to pivot element, if 
// we find such element swap elements at index i and j. Increment j value only on swap. Continue this until i 
// reaches end of array. This gives the final index of pivot element in the sorted array.

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
       int j = 0;
       for(int i=0;i<=h;i++){
           if(arr[i]<=pivot){
              swap(arr, i, j);
              j++;
           }
       }
       return --j;
    } 

    int[] createArray(int l,int h){
        int[] e = new int[]{l,h};
        return e;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> s = new Stack<int[]>();
        int pivot = partition(arr, l, h);
        s.addElement(createArray(pivot+1, h));
        s.addElement(createArray(l, pivot-1));
        int left;
        int right;
        while(s.size() > 0){
            pivot = partition(arr, s.peek()[0], s.peek()[1]);
            left = s.peek()[0];
            right = s.peek()[1];
            s.pop();
            if(pivot+1<right){
                s.push(createArray(pivot+1, right));
            }
            if(left<pivot-1){
                s.push(createArray(left, pivot-1));
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