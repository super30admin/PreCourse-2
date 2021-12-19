// Time Complexity :O(n^2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :  N/A
// Any problem you faced while coding this : Array Index Out of Bounds

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[],int position, int start, int end) 
    { 
    	int l = start;
    	int h = end-2;
    	int piv = arr[position];
    	swap(arr, position, end-1);
    	while (l < h) {
    		if (arr[l] < piv) {
    			l++;
    		} else if (arr[h] > piv) {
    			h--;
    		} else {
    			swap(arr, l, h);
    		}
    	}
    	int idx = h;
    	if (arr[h] < piv) {
    		idx++;
    	}
    	swap(arr, end - 1, idx);
    	return idx;
    	
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    	Stack<Integer> stack = new Stack(); 
    	stack.push(l);
    	stack.push(h); 
    	while (!stack.isEmpty()) {
    		int end = stack.pop(); 
    		int start = stack.pop(); 
    		if (end - start < 2) {
    			continue;
    		} 
    		int p = start + ((end - start) / 2); 
    		p = partition(arr, p, start, end); 
    		stack.push(p + 1); 
    		stack.push(end); 
    		stack.push(start); 
    		stack.push(p);
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