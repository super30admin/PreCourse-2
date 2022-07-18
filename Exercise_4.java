// Time Complexity : O(nlog n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : no


/*Your code here along with comments explaining your approach -- Divide and concur
•    Declare left variable to 0 and right variable to n-1 
•    Find mid by medium formula. mid = (left+right)/2
•    Call merge sort on (left,mid)
•    Call merge sort on (mid+1,rear)
•    Continue till left is less than right
•    Then call merge function to perform merge sort.
*/



class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
    	//sizes of the left sub array and right sub array
    	int leftLen = m-l+1;
    	int rightLen = r-m;
    	
    	//creating the temp left sub array and right sub array
    	int left[] = new int[leftLen];
    	int right[] = new int[rightLen];
    	
    	for(int i=0;i<leftLen;i++) {
    		left[i] = arr[l+i];
    	}
    	
    	for(int j=0;j<rightLen;j++) {
    		right[j] = arr[m+1+j];
    	}
    	
    	//indexes of the right , left and merged array
    	int i=0,j=0,k=l;
    	
    	while(i<leftLen && j<rightLen) {
    		if(left[i]<=right[j]) {
    			arr[k]=left[i];
    			i++;
    		}
    		else {
    			arr[k]=right[j];
    			j++;
    		}
    		k++;
    	}
    	
    	while(i<leftLen) {
    		arr[k] = left[i];
    		i++;
    		k++;
    	}
    	
     	while(j<rightLen) {
    		arr[k] = right[j];
    		j++;
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
    		int mid = (l+r)/2;
    		
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
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 