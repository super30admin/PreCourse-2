
//TC: O(nLogn)
//SC: O(n)

package problems;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
	
	
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	
    	//find size of two subarrays to be merged
    	int n1 = m - l + 1;
    	int n2 = r - m;
    	
    	//Create temp arrays
    	int Left[] = new int[n1];
    	int Right[] = new int[n2];
    	
    	//copy data into temp arrays
    	for(int i = 0; i < n1; ++i) {
    		Left[i] = arr[l + i];
    	}
    	for(int j = 0; j < n2; ++j) {
    		Right[j] = arr[m + 1 + j];
    	}
    	
    	//Merger the temp arrays
    	
    	//initial indexes of first and second subarrays
    	
    	int i = 0, j = 0;
    	
    	//Initial index of merged subarray arr
    	int k = l;
    	while(i < n1 && j < n2) {
    		if(Left[i] <= Right[j]) {
    			arr[k] = Left[i];
    			i++;
    		} else {
    			arr[k] = Right[j];
    			j++;
    		}
    		k++;
    	}
    	
    	//copy remaining elements of Left[] if any
    	
    	while(i < n1) {
    		arr[k] = Left[i];
    		i++;
    		k++;
    	}
    	
    	//copy remaining elements of Right[] if any
    	
    	while(j < n2) {
    		arr[k] = Right[j];
    		j++;
    		k++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l < r) {
    		int mid = l + (r - l)/2;
    		sort(arr, l, mid);
    		sort(arr, mid + 1, r);
    		
    		//merge the sorted two halves
    		merge(arr, l, mid, r);
    	}
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
}