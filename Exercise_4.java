class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int a1 = m-l+1;
       int a2 = r-m;
       
       int F[] = new int[a1];
       int S[] = new int[a2];
       
      // copying data into temp array
       for(int i=0; i<a1;i++)
    	   F[i] = arr[l+i];
       for(int j=0;j<a2;j++)
    	   S[j] = arr[m+j+1];
       
       int i=0,j=0;
       
       int k=l;
       
       while(i<a1 && j<a2)
       {
    	   if(F[i] <= S[j])
    	   {
    		   arr[k] = F[i];
    		   i++;
    	   }
    	   else 
    	   {
    		   arr[k] = S[j];
    		   j++;
    	   }
    	   
    	   k++;
       }
       
       while(i<a1)
       {
    	   arr[k] = F[i];
    	   i++;
    	   k++;
       }
       
       while(j<a2)
       {
    	   arr[k] = S[j];
    	   j++;
    	   k++;
       }
    	   
    } 
  
  
    void sort(int arr[], int l, int r) 
    { 
	   if(l<r)
	   {
		   int m = (l+r)/2;
		   
		   sort(arr, l, m);
		   sort(arr, m+1,r);
		   
		   merge(arr, l,m,r);
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
