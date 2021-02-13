class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
	//Time Complexity: O(nlogn)
	//Space Complexity: O(n)
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
    	int tempArr[] = new int[r-l+1];
    	int p1 = l;
    	int p2 = m+1;
    	int i = 0;
    	while(p1 <= m && p2 <= r) {
    		if(arr[p1]<=arr[p2]) {
    			tempArr[i++]=arr[p1++];
    		}
    		else {
    			tempArr[i++]=arr[p2++];
    		}
    	}
    	while(p1<=m) {
    		tempArr[i++]=arr[p1++];
    	}
    	while(p2<=r) {
    		tempArr[i++]=arr[p2++];
    	}
    	i = 0;
    	for(int index = l; index<=r; index++) {
    		arr[index] = tempArr[i++];
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l<r) {
    		int mid = l+ (r-l)/2;
    		//sort two sub-arrays
    		sort(arr, l, mid);
    		sort(arr, mid+1, r);
    		//merge the sub-arrays
    		merge(arr,l,mid,r);
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