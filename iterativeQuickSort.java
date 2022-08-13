//Precourse 2: Exercise 5   --  Iterative QuickSort
// Time Complexity : O(n log n) because it atomizes all elements once which takes log n but it happens n times
// Space Complexity : O(n) for storing n elements also as this sorting technique is in place.
// Any problem you faced while coding this : no

/*Output:
Given Array
4 3 5 2 1 3 2 3 
Sorted Array
1 2 2 3 3 3 4 5 
 */

import java.util.*;

public class iterativeQuickSort {

	void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
		//System.out.println("\nThe initial values of i an j are:"+ arr[i]+ arr[j]);
		if(arr[i]!= arr[j]) {
		arr[i]=arr[i]+arr[j];
		arr[j]=arr[i]-arr[j];
		arr[i]=arr[i]-arr[j];
		
		/* int temp=arr[i];
		 arr[i]=arr[j];
		 arr[j]=temp;*/
		//System.out.println("The after values of i an j are:"+  arr[i]+ arr[j]);
		}
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot=arr[h];
    	int i=l-1;
    	for(int j=l; j<= h-1; j++)
    	{
    		if(arr[j]<= pivot)
    		{
    			i++;
    			swap(arr, i, j);
    		}
    	}
    	swap(arr, i+1, h);
    	return i+1;
    	
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void sort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h - l + 1];
 
        // initializing top of stack
        int top = -1;
 
        // push initial values of l and h to stack
        stack[++top] = l;
        stack[++top] = h;
 
        // Keep popping from stack while it is not empty
        while (top >= 0) {
            // Pop h and l
            h = stack[top--]; //pop and work on that range from l to h
            l = stack[top--];
 
            // Set pivot element at its correct position in sorted array
            int pindex = partition(arr, l, h);
 
            // If there are elements on left side of pivot then push left side to stack and work on that range after popping
            if ((pindex - 1) > l) {
                stack[++top] = l;
                stack[++top] = pindex - 1;
            }
 
            // If there are elements on right side of pivot then push right side to stack and work on that range after popping
            if ((pindex + 1) < h) {
                stack[++top] = pindex + 1;
                stack[++top] = h;
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
    	iterativeQuickSort ob = new iterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        System.out.println("Given Array"); 
        ob.printArr(arr, arr.length); 
        ob.sort(arr, 0, arr.length - 1); 
        System.out.println("\nSorted Array");
        ob.printArr(arr, arr.length); 
    } 
	
}
