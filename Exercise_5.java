// Time Complexity : O(NLogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this :

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	    arr[i] = arr[i]+arr[j];
	    arr[j] = arr[i]-arr[j];
	    arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
	    int pivot = arr[h];
	    int i = low-1;
	    for (int j = low; j < high; j++) {
            if (array[j] < pivot) {
                i++;
             swap(arr,i,j);
	    }
	}
	    swap(arr,i,j);

	    return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
	    if(l==h) return;
	    Stack<Integer> st = new Stack<>();
	    stack.push(l);
	    stack.push(h);
            while(!stack.isEmpty()){
		    h= stack.pop();
		    l = stack.pop();

	    int partitionIndex = partition(array,l,h);

            // Push elements smaller than the pivot
            if (partitionIndex - 1 > low) {
                stack.push(low);
                stack.push(partitionIndex - 1);
            }

            // Push elements greater than the pivot
            if (partitionIndex + 1 < high) {
                stack.push(partitionIndex + 1);
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
