//Complexities
//Time: O(n log n)
//Space: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //create 2 new left and right sub arrays from input
    	
    	int n1 = m - l + 1;
    	int n2 = r - m;
    	
    	int[] L = new int[n1];
    	int[] R = new int[n2];
    	
    	//copy elements
    	for(int i = 0; i < n1; i++) {
    		L[i] = arr[l + i];
    	}
    	
    	for(int j = 0; j < n2; j++) {
    		R[j] = arr[m + 1 + j];
    	}
    	
    	//merge L and R arrays to original
    	
    	int k = l;
    	int i = 0, j = 0;
    	
    	while(i < n1 && j < n2) {
    		if(L[i] <= R[j]) {
    			arr[k] =  L[i];
    			i++;
    		}
    		else {
    			arr[k] = R[j];
    			j++;
    		}
    		k++;
    	}
    	//copy remaining elements
    	while(i < n1) {
    		arr[k] = L[i];
    		k++;
    		i++;
    	}
    	
    	while(j < n2) {
    		arr[k] = L[j];
    		k++;
    		j++;
    	}
    	
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	if(l < r) {
    		
    		//find mid point
    		int mid = l + (r - l)/2;
    		//sort start to mid and mind to end
    		sort(arr, l, mid);
    		sort(arr, mid + 1, r);
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