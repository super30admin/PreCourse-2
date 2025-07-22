class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    // Time Complexity: O(nlog(n))
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int lsize = m-l+1;
       int rsize = r-m;

       int lsubarr[] = new int[lsize];
        int rsubarr[] = new int[rsize];

        for(int i=0;i<lsize;++i)
            lsubarr[i] = arr[l+i];
        for(int i=0;i<rsize;++i)
            rsubarr[i] = arr[m+i+1];
        
        //merge arrays
        int i=0,j=0;
        int k=l;
        //replace the original array elements based on comparing both left and right sub-arrays.
        while(i<lsize && j<rsize)
        {
            if(lsubarr[i]<=rsubarr[j])
            {
                arr[k] = lsubarr[i];
                i++;
            }
            else{
                arr[k] = rsubarr[j];
                j++;
            }
            k++;
        }
        
        //replace original array elements if any sub array elements left.
        while(i<lsize)
        {
            arr[k] = lsubarr[i];
            i++;
            k++;
        }

        while(i<rsize)
        {
            arr[k] = rsubarr[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r)
        {
            int m = l+(r-l)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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
    // Time Complexity: O(nlog(n))
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