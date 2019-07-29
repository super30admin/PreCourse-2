class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    static void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    		int n1, n2;
    		n1 = m-l+1;
    		n2 = r-m;
    		
    		int[] L = new int[n1+1];
    		int[] R = new int[n2+1];
    		
    		for(int i=0; i<n1 ; i++) {
    			L[i] = arr[l+i];
    		}
    		L[n1] = Integer.MAX_VALUE;
    		
    		for(int i=0; i<n2 ; i++) {
    			R[i] = arr[m+1+i];
    		}
    		R[n2] = Integer.MAX_VALUE;
    		int i=0, j=0, k=l;
    		while(k <= r) {
    			if(L[i] <= R[j]) {
    				arr[k] = L[i];
    				i++;
    			} else {
    				arr[k] = R[j];
    				j++;
    			}
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
    			//Splitting the array into two sets
    			int m = l+ (r-l)/2;
    			
    			//Sorting each of the sets
    			sort(arr, l, m);
    			sort(arr, m+1, r);
    			
    			//Merging the two sorted sets
    			merge(arr, l, m, r);
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