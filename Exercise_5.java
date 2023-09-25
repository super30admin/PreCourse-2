// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : -
/* Any problem you faced while coding this : 
 * Need help with the following:
 * 1. Not able to visualize the logic using Stack data structure
 * 2. Swapping without using extra variables  */

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	
    /*	This works
     * int x = 10;
        int y = 5;
        x = x + y;
        y = x - y;
        x = x - y;
        System.out.println("After swapping:" + " x = " + x + ", y = " + y);*/
                           	
    /*	But, this doesnot work
     * arr[i] = arr[i] + arr[j];
    	arr[j] = arr[i] - arr[j];
    	arr[i] = arr[i] - arr[j];*/
    	
    	arr[i] = (arr[i] * arr[j])/(arr[j] = arr[i]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot = arr[h];
    	int i = l-1;
    	
    	for(int j = l; j< h; j++) {
    		if(arr[j] <= pivot) {
    			i++;
    			swap(arr, i, j);
    		}
    	}
		swap(arr, i+1, h);
    	return (i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> stack = new Stack<Integer>();
    	
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