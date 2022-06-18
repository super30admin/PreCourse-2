//Time Complexity : O(n^2)
//Space Complexity : O(n) 
//Did this code successfully run on Leetcode : Yes 
import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	int t = arr[i];
    	arr[i] = arr[j];
    	arr[j] = t;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
    	int p = arr[high];
    	int i=low-1;
    	for(int j=low;j<high;j++)
    	{
    		if(arr[j]<p)
    		{
    			i++;
    			swap(arr, i, j);
    		}
    	}
    	
    	swap(arr, i+1, high);
    	
    	return i+1;
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
    			int high = stack.pop();
    			int low = stack.pop();
    			
    			int pivot = partition(arr ,low, high);
    			if(low<pivot-1)
    			{
    				stack.push(low);
        			stack.push(pivot-1);
    			}
    			if(pivot+1<high)
    			{
    				stack.push(pivot+1);
        			stack.push(high);
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