//package precourse2;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
     
      //Tried doing merging without creating new sub-arrays but took long time and was not successful 
      int[] left  = new int[m - l + 1];
      int[] right = new int[r - m ];
      
      for(int i = 0; i<left.length;i++) {
    	  left[i] = arr[l+ i]; 
      }
      
      for(int j = 0; j<right.length;j++) {
    	  right[j] = arr[m + j + 1];
     }
      
      int count = l;
      int i = 0;
      int j = 0;
      while(i < left.length && j < right.length) {
    	  if(left[i]<=right[j]) {
    		  arr[count] = left[i];
    		  i++;
    		  count++;
    		  //j--;
    	  }else {
    		  arr[count] = right[j];
    		  j++;
    		  count++;
    		  //i++;
    	  }
    	  
      } 
    	  while(i < left.length) {
    		  arr[count] = left[i];
    		  i++;
    		  count++;
    	  }
    	  
    	  while(j < right.length) {
    		  arr[count] = right[j];
    		  j++;
    		  count++;
    	  }
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	if(l < r) {
    		//Write your code here
            //Call mergeSort from here 
        	int mid = (l + r)/2;
        	sort(arr,l,mid);
        	sort(arr,mid+1,r);
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
        int arr[] = {12, 11, 13,5,6} ;//, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 