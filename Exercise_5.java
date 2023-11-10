// Time Complexity : O(NlogN) N is the number of elements in the array.
// Space Complexity : O(N) for stack
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach

import java.util.Stack;

/**
 * @author akhilreddy619
 * In quick sort, we have to partition the array into two parts every time by finding
 * pivot index which separates smaller elements on one side and bigger elements (than pivot)
 * on the other side. To find pivot index, we consider last element as pivot element. And we
 * maintain a variable to track the index of the smaller elements that are less than pivot element with i.
 * Then iterate over from low to high - 1 elements to check if any element is <= pivot.
 * If found, we swap the current index with ith index. After all iterations we swap i+1th 
 * index with pivot such that pivot separates smaller elements and bigger elements than the pivot.
 * Repeat the process for the elements ranging from (low, pivot index - 1) and (pivot index + 1, high).
 * In iterative approach, we push the (l, h) pair to a stack. while the stack is not empty, we pop these
 * pairs and find the partition. if each side has more than 1 element, then we push those ranges (l, partition - 1)
 * and (partition + 1, h) to the stack. This process goes on until stack is empty.
 */
class IterativeQuickSort { 
	// Note: Used swap logic without third variable but in this case, it didn't work
	// in case of where i and j are same. 
	// Actual logic: a = a + b; b = a - b; a = a - b;
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
    	int i = l - 1;
    	for(int j=l; j<= h-1;j++) {
    		if(arr[j] <= pivot) {
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
    	Stack<int[]> stack = new Stack<>();
    	stack.push(new int[] {l, h});
    	while(!stack.isEmpty()) {
    		int[] p = stack.pop();
    		int part = partition(arr, p[0], p[1]);
    		if(part - 1 > p[0])
    			stack.push(new int[] {l, part-1});
    		if(part + 1 < p[1])
    			stack.push(new int[] {part+1, h});
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