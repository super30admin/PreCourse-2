package precourse2;
import java.util.*;

public class IterativeQuickSort2 {
	 void swap(int arr[],int i,int j){
	     //Your code here   
		 int temp = arr[j];
		 arr[j] = arr[i];
		 arr[i] = temp;
	 }
  
    /* This function is same in both iterative and 
       recursive*/
	 int partition(int arr[], int low, int high) 
	 { 
		//Write code here for Partition and Swap 
		 int pivot = arr[high];
		 int i = low -1;
		 for (int j=low; j<=high-1;j++) {
			 
			 if (arr[j]<pivot) {
				 i++;
				 swap(arr, i, j);
			 }			 
		 }
		 swap(arr,i+1, high);
		 
		 
		 return i+1;
	 } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack s = new Stack();
    	s.push(l);
    	s.push(h);
    	
    	int partitionIndex;
    	int low;
    	int high;
    	while(!s.isEmpty()) {
    		
    		high = (int)s.pop();
    		low = (int)s.pop();
    		
    		partitionIndex = partition(arr, low, high);
    		
    		if (partitionIndex-1>low) {
    			s.push(low);
    			s.push(partitionIndex-1);
    		} 
    		if (partitionIndex+1<high) {
    			s.push(partitionIndex+1);
    			s.push(high);
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
        IterativeQuickSort2 ob = new IterativeQuickSort2(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
    
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 

}
