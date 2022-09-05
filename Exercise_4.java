// time complexity is O(nlog n), as dividing the array is o(log n) and merging takes O(n)
// space complexity :  we have used 2 temp arrays, so space complexity is O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
    	int lasize = m-l+1;
    	int rasize=r-m;
    	int[] left= new int[lasize];
    	int[] right= new int[rasize];
   
    	
    	for(int i=0;i<lasize;i++) {
    		left[i]=arr[l+i];
    	}
    	
    	for(int j=0;j<rasize;j++) {
    		right[j]=arr[m+1+j];
    	}
    	
    	//  Merge the temp arrays
    	int i=0,j=0,k=l;
    	while(i<lasize && j<rasize) {
    		if(left[i]<=right[j]) {
    			arr[k]=left[i];
    			i++;
    			k++;
    		}
    		else {
    			arr[k]=right[j];
    			j++;
    			k++;
    		}
    	}
    	 // Copy remaining elements of left[]
    	while(i<lasize) {
    		arr[k]=left[i];
			i++;
			k++;
    	}
    	
   	 // Copy remaining elements of right[]
    	while(j<rasize) {
    		arr[k]=right[j];
			j++;
			k++;
    	}
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