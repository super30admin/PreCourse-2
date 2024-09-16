class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    	int leftLength = m-l+1;
    	int rightLength = r-m;		
    	int arrL[] = new int[leftLength];
    	int arrR[] = new int[rightLength];

    	for(int i = 0;i<leftLength;i++) {
    		arrL[i] = arr[l+i];
    	}
    	for(int j = 0;j<rightLength;j++) {
    		arrR[j] = arr[m+j+1];
    	}
    	
    	int p=0,q=0;
    	int k = l;
    	while(p<arrL.length && q<arrR.length) {
    		if(arrL[p] <= arrR[q]) {
    			arr[k] = arrL[p];
    			p++;
    		}else {
    			arr[k] = arrR[q];
    			q++;
    		}
    		k++;
    	}
    	
    	while(p<arrL.length) {
    		arr[k] = arrL[p];
    		p++;
    		k++;
    	}
    	
    	while(q<arrR.length) {
    		arr[k] = arrR[q];
    		q++;
    		k++;
    	}
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l<r) {
    		int m = (l+r)/2;
    		
    		sort(arr,l,m);
    		sort(arr,m+1,r);
    		
    		merge(arr,l,m,r);    		
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