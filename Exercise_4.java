//Time complexity : O(n* logn)
//space complexity : O(n)
import java.util.Arrays;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	
         int[] leftsubarr = Arrays.copyOfRange(arr, l, m+1);
         //System.out.println("copy  own "+Arrays.toString(lef));
         
    	 int[] rightsubarr = Arrays.copyOfRange(arr, m+1,r+1);
    	
    	 
    	int i = 0, j=0, k =l;
    	
    	while(i < leftsubarr.length && j < rightsubarr.length )
    	{
    		if(leftsubarr[i] <= rightsubarr[j])
    		{
    			arr[k] = leftsubarr[i];
    			i++;
    		}else
    		{
    			arr[k] = rightsubarr[j];
    			j++;
    		}
    		k++;
    	}
    	while(i < leftsubarr.length)
    	{
    		arr[k] = leftsubarr[i];
			i++;k++;
    	}
    	
    	while(j < rightsubarr.length)
    	{
    		arr[k] = rightsubarr[j];
			j++;k++;
    	
    	}
    	
    	
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	     //Write your code here
        //Call mergeSort from here 
          
        if(l < r)
        {
            int mid = l + (r-l)/2;
            
            sort(arr, l, mid);
            
            sort(arr, mid+1, r);
            
            merge(arr, l,mid,r);
            
            
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