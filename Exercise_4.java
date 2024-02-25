// Time Complexity : O(NlogN)
// Space Complexity : O(N)+O(logN)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  

	int[] sortedArray = new int[r-l+1];
	int currIndex = 0;
	int i=l;
	int j = m+1;

	    while(i<=m && j<=r){
		    if(arr[i]<arr[j]){
			   sortedArray[currIndex]=arr[i];
			    i++
		    }
		    else{
			    sortedArray[currIndex] = arr[j];
			    j++;
		    }
	    }

	      while(i<=m){  
		      sortedArray[currInd++]=arr[i++];
	      }
        while(j<=r){
		sortedArray[currInd++]=arr[j++];
	}

	     for(currIndex=0;currIndex<sortedArr.length;currIndex++) {
		     arr[l+currIndex]=sortedArray[currIndex];
	     }
	    
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

	    if(l==r) return;

	    int mid = l+(r-l)/2;
	    sort(arr,l,mid);
	    sort(arr,mid+1,right);

	    merge(arr,l,mid,r);
	    
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
