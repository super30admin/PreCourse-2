// Time Complexity : O(N^2)
// Space Complexity :O(N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
       if(arr[i]!=arr[j]) {
        arr[i] = arr[i]*arr[j];
        arr[j] = arr[i]/arr[j];
        arr[i]=arr[i]/arr[j];
       }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int p=arr[h];
        int i=l-1;
        for(int j=l; j<h; j++){
            if(arr[j]<=p){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	 Stack<Integer> stack=new Stack();


 		// push array values of l and h
 		stack.push(l);
 		stack.push(h);

 		// pop from stack till it's not empty
 		while (!stack.isEmpty()) {
 		
 			 h= stack.pop();
 			 l= stack.pop();

 			int pos=partition(arr, l, h);

 			if (pos-1>l) {
 				stack.push(l);
 				stack.push(pos-1);
 			}

 			if (pos+1< h) {
 				stack.push(pos+1);
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