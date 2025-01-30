// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
	int n=r-l+1;
          int[] newarr=new int[n];
          int p=l;
          int q=m+1;
          int i=0;
          while(i<n && p<=m && q<=r) {
        	  if(arr[p]<=arr[q]) {
        	      newarr[i]=arr[p];
        	      p++;
        	  }else {
        	      newarr[i]=arr[q];
        	      q++;
        	  }
        	  i++;
          }
          while(p<=m) {
             newarr[i]=arr[p];
             i++;
             p++;
          }
          while(q<=r) {
              newarr[i]=arr[q];
              i++;
              q++;
           }
          int start=l;
          for(int j=0;j<n;j++) {
              arr[start]=newarr[j];
              start++;
          }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
	if(l<r) {
	    int mid=l+(r-l)/2;
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
        int arr[] = {12, 11, 14, 13, 2, 14}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 