//Time Complexity : O(nlog), we have sort function which is being called recursively, 
//which would keep on dividing the array, so complexity of that is O(logn), the merge subroutine merges the arrays in linear fashion , so time complexity of that is O(n)
//Space Complexity :O(n) It is a recursive function , which means it will use a call stack, which can take upto O(logn) space in best case. For merge subroutine we are creating a new array of size of the same array or smaller, so space would be O(n) for that
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this : The merge subroutine was difficult to implement, I was first modifying the original array, then I put the result in new array and then appended its value to the original array


//Your code here along with comments explaining your approach


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
      
    	
    	int low =l; // low should go from low to m
    	int high =m+1; // high will go from m+1 to r
    
    	// creating a new array, and will put sorted values in that array
    	
    	int[] arrNew = new int[arr.length];
    	int pos = l; // position on the new array pointer
    	
    	while(low <= m && high <= r) { 
    		// lower value would be in the position
    		if(arr[low] <= arr[high]) {
    			arrNew[pos++] = arr[low++];
    		}
    		else {
    			arrNew[pos++] = arr[high++];
    		}
    	}
    	
    	// check if anything is left, if so then add it to the resulting array
    	
    	while(low <= m) { 
    		arrNew[pos++] = arr[low++];
    	}
    	while(high <= r) { 
    		arrNew[pos++] = arr[high++];
    	}
    	
    	
    	// copying value from the new array back to the original array
    	
    	for (int i=l; i<=r;i++) { 
    		arr[i] = arrNew[i];
    	}
    	
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	
    	
    	if(l<r) { // we would divide until we have a single element i.e when l==r
    		
    		int mid = (l+r)/2; // find the mid point to split the array in half
    		
    		sort(arr,l,mid);  // further divide the left half
    		sort(arr,mid+1,r); // further divide the right half
    		merge(arr,l,mid,r); // merge left and right
    		
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