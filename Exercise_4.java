//Time Complexity-O(logn)
//Space Complexity-O(1)
// Problem : issues in understanding complexity analysis

class MergeSort 
{
	 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int[] mix = new int[r-l];
    	
    	int i = l ;
    	int j = m ;
    	int k = 0 ;
    	
    	while(i<m && j < r) {
    		
    		if(arr[i] < arr[j]) {
    			mix[k] = arr[i];
    			i ++ ;
    		}
    		else {
    			mix[k] = arr[j];
    			j ++ ;
    		}
    		k++ ;
    	}
    	
    	while(i<m) {
    		mix[k] = arr[i] ;
    		i++;
    		k++ ;
    	}
    	while(j<r) {
    		mix[k] = arr[j] ;
    		j++;
    		k++ ;
    	}
    	for(int a = 0; a< mix.length ; a++ ) {
    		arr[l+a] = mix[a];
    	}
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(r-l == 1) {
    		return ;
    	}
    	int mid = (l+r) / 2;
    	sort(arr, l , mid) ;
    	sort(arr, mid , r) ;
    	merge(arr, l , mid ,r);     	
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
        ob.sort(arr, 0, arr.length); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 


} 