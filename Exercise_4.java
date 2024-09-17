class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int ll = m-l+1;
    	int al[] = new int[ll];
    	for(int i=0;i<ll;i++) {
    		al[i] = arr[l+i];
    	}
    	
    	int rl = r-m;
    	int ar[] = new int[rl];
    	for(int i=0;i<rl;i++) {
    		ar[i] = arr[m+i+1];
    	}
    	
    	int i=0;
    	int j=0;
    	int t=l;
    	
    	while(i<ll&&j<rl) {
    		if(al[i]<ar[j]) {
    			arr[t] = al[i];
    			i++;
    		} else {
    			arr[t] = ar[j];
    			j++;
    		}
    		t++;
    	}
    	
    	while(i<ll) {
    		arr[t] = al[i];
			i++;
			t++;
    	}
    	while(j<rl) {
    		arr[t] = ar[j];
			j++;
			t++;
    	}
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l<r) {
    		int m = l+(r-l)/2;
    		sort(arr, l, m);
    		sort(arr, m+1, r);
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