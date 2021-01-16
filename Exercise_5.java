//Complexities
// Time: worst case: O(n^2); avg: O(n log n)
// Space: O(n) for stack 

import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	//arr[i] = 5;
    	//arr[j] = 10;
	//Try swapping without extra variable 
    	if(i != j) {
    		arr[i] = arr[i] + arr[j]; //15
        	arr[j] = arr[i] - arr[j]; //5
        	arr[i] = arr[i] - arr[j]; //10
    	}  	    	
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = l;
        
        for(int j = l; j < h; j++) { 
    		//swap if current is smaller than pivot 
    		if(arr[j] < pivot) { 
    			swap(arr, i, j); 
    			i++; 
    		} 
    	} 
    	//now swap pivot and arr[i] 
    	swap(arr, i, h); 
    	 
    	//return position of pivot 
    	return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> st = new Stack<Integer>();
    	st.push(l);
    	st.push(h);
    	
    	//while st is not empty
    	while(!st.isEmpty()) {
    		h = st.pop();
    		l = st.pop();
    		
    		//get the pivot position from sorted
    		int pivot = partition(arr, l, h);
    		
    		//if elements on left side of arr, push
    		if(pivot - 1 > l) {
    			st.push(l);
    			st.push(pivot - 1);
    		}
    		
    		//if elements on right side of arr, push
    		if(pivot + 1 < h) {
    			st.push(pivot + 1);
    			st.push(h);
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