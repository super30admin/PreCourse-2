//package precourse2;

import java.util.Stack;




class IterativeQuickSort { 
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
    	//Write code here for Partition and Swap
    	int pivot = arr[h];
    	int i = l;
    	for(int j = l; j<=h; j++) {
    		if(pivot > arr[j]) {
    			swap(arr,i,j);
    			i++;
    		}
    	}
    	
    	swap(arr,i,h);
    	return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> s = new Stack<>();
    	//Pair<Integer, Integer> pair = Pair.with(l,h);
    	s.push(l);
    	s.push(h);
    	
    	while(!s.isEmpty()) {
    		int new_h = s.pop();
    		int new_l = s.pop();
    		int pivotElement = partition(arr,new_l,new_h);
    		
    		if((new_l < pivotElement - 1)) { //|| (new_h > pivotElement + 1) {
    			s.push(new_l);
    			s.push(pivotElement - 1);
    		}
    		
    		if(new_h > pivotElement + 1) {
    			s.push(pivotElement + 1);
    			s.push(new_h);
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
        //int arr[] = {6, 5, 4, 3, 2, 1};
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 