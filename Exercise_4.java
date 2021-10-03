class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int temp[] = new int[a.length];
    	
    	int leftEnd = (leftStart+rightEnd)/2;
    	int rightStart = leftEnd +1;
    	int size = rightEnd-leftStart+1;
    	
    	int left = leftStart;
    	int right = rightStart;
    	int index = leftStart;
    	
    		while(left<=leftEnd && right <= rightEnd) {
    			if(a[left]<=a[right]) {
    				temp[index] = a[left];
        			
        			left++;
    			} else {
    				temp[index] = a[right];
        			right++;
    			}
    			index++;
    			
    		}
    	
    	System.arraycopy(a, left, temp, index, leftEnd-left+1);
    	System.arraycopy(a, right, temp,index, rightEnd-right+1);
    	
    	System.arraycopy(temp,leftStart,a,leftStart,size);
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r) {
    		return;
    	}
    	int mid = (l+r)/2;
    	
    	sort(arr,l,mid);
    	sort(arr,mid+1,r);
    	merge(arr,l,r);
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