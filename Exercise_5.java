// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 

        if(i==j) return;  // Need to do this to avoid unsigned memory operations issues 
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];

    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
         int pivot=arr[h]; // Pivot to last element in an array

        int i=l;           // Fix pointer i to low element

        for(int j=l;j<h;j++){ // Iterate between low and high

            if(arr[j]<pivot){    // If element is less than pivot then swap current element with smaller element and increment smaller element(i)

                swap(arr,i,j);   
                i++;
            }
                                // else do nothing. Keep incrementing j pointer
        }

       swap(arr,i,h);        // swap last element i with high/pivot to fix pivot in correct position such that all elements left of pivot are small
                                // and all elements right of pivot are greater.

        return i;              // i points to actual index position of pivot
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 

       Stack<Integer> stack = new Stack<>(); // create a stack of integer

        stack.push(l);                  // push low and high values into stack initially
        stack.push(h);

        while (!stack.isEmpty()) {

            h=stack.pop();             // pop high and low elements from stack
            l = stack.pop();

            int index = partition(arr, l, h); // Partition array with low and highs

            if (index - 1 > l) {                // check if any elements left side of pivot which are smaller then push to stack
                stack.push( l);
                stack.push( index - 1);
            }

            if (index + 1 < h) {        // check if any elements right side of pivot which are greater then push to stack
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