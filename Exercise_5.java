//TC - O(nlogn)
//SC - O(n)

import java.util.*;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
	    int tmp = arr[i];
	    arr[i] = arr[j];
	    arr[j] = tmp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    { 
        //Compare elements and swap.
	    int pivot = arr[high], i = low - 1;
	    for(int j = low; j <= high-1; j++){
		    if(arr[j] < pivot){
			    i++;
			    swap(arr,i,j);
		    }
	    }
	    swap(arr,i+1,high);
	    return i+1;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high)
    { 
        //Try using Stack Data Structure to remove recursion.
	    Stack<int[]> stack = new Stack<>();
		stack.push(new int[]{low, high});
	    while(!stack.isEmpty()){
			int tmp[] = stack.pop();
			low = tmp[0];
			high = tmp[1];
			if(low < high) {
				int pivot = partition(arr, low, high);
				stack.push(new int[] { low, pivot - 1 });
				stack.push(new int[] { pivot + 1, high });
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