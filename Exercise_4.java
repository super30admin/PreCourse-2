class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int arrTemp[] = new int[r-l+1];
       int i = l;
       int j = m+1;
       int k = 0; 
       while(i <= m && j <= r) {
		if(arr[i] <= arr[j]) {
			arrTemp[k] = arr[i];
			k += 1; i += 1;
		}
		else {
			arrTemp[k] = arr[j];
			k += 1; j += 1;
		}
	}

       while(i <= m) {
		arrTemp[k] = arr[i];
		k += 1; i += 1;
	}

	// add elements left in the second interval 
	    while(j <= r) {
		    arrTemp[k] = arr[j];
		    k += 1; j += 1;
	}

       for(i = l; i <= r; i += 1) {
		arr[i] = arrTemp[i - l];
	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    //Call mergeSort from here 
    while (l<r){
        int mid = (l+r)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
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