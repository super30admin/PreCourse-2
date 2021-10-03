
import java.util.*;

public class IterativeQuickSort {

	 void swap(int arr[], int i, int j) 
	    { 
		//Try swapping without extra variable 
		 int x=arr[i];
		 arr[i]=arr[j];
		 arr[j]=x;
	    } 
	  
	    /* This function is same in both iterative and 
	       recursive*/
	    int partition(int arr[], int l, int h) 
	    { 
	        //Compare elements and swap.
	    	 int x=arr[h];
	    	 int i=l-1;
	    	 int j=l;
	    	 while(j<h) {
	    		 if(arr[j]<x) {
	    			 swap(arr,++i,j);
	    		 }
	    		 j++;
	    	 }
	    	 swap(arr,++i,h);
	    	 return i;
	    } 
	  
	    // Sorts arr[l..h] using iterative QuickSort 
	    void QuickSort(int arr[], int l, int h) 
	    { 
	        //Try using Stack Data Structure to remove recursion.
	    	Stack <Integer> stack = new Stack();
	    	stack.push(l);
	    	stack.push(h);
	    	int high;
	    	int low;
	    	int index;
	    	while(!stack.isEmpty()) {
	    		high=stack.pop();
	    		low=stack.pop();
	    		index=partition(arr,low,high);
	    		if(index-1>low) {
	    			stack.push(low);
	    			stack.push(index-1);
	    		}
	    		if(index+1<high) {
	    			stack.push(index+1);
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
