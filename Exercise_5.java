import java.util.*;

class IterativeQuickSort { 
	
	//Time Complexity O(1)
	//Space Complexity O(1)
    void swap(int arr[], int i, int j) 
    { 
    	if(i==j) {
    		return;
    	}
    	arr[i]= arr[i]^ arr[j];
    	arr[j]= arr[i]^ arr[j];
    	arr[i]=arr[i]^ arr[j];
    	
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    //Time Complexity O(n)
    //Space Complexity O(1)
    int partition(int arr[], int l, int h) 
    { 
    	int pivot= arr[h];
    	int index= l-1;
    	for (int j= l;j<h;j++){
    		if(arr[j]<=pivot) {
    			index++;
    			swap(arr,index,j);
    		}
    	}
    	swap(arr,index+1,h);
    	return index+1;
        //Compare elements and swap.
    } 
  
    
    //Have doubt analyzing space and time complexities
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    	Stack<Integer> s= new Stack<>();
    	
    	s.push(l);
    	s.push(h);
    	
    	while(!s.isEmpty()) {
    		h=s.pop();
    		l=s.pop();
    		
    		int pIndex= partition(arr,l,h);
    		
    		if(pIndex-1>l) {
    			s.push(l);
    			s.push(pIndex-1);
    		}
    		
    		if(pIndex+1<h) {
    			s.push(pIndex+1);
    			s.push(h);
    		}
    		
    	}	
    	
        //Try using Stack Data Structure to remove recursion.
    } 
  
    //Time Complexity O(n)
    //Space Complexity O(1)
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