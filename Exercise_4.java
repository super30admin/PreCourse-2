class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int[] arr1 = new int[arr.length];
       System.arraycopy(arr, l, arr1, l, r-l+1);
       int i = l, k=l, j=m+1;
       while(i<=m && j<=r)
       {
           if(arr1[i]<=arr1[j])
           {
               arr[k++] = arr1[i++];
           }
           else{
               arr[k++]=arr1[j++];
           }
       }
       while(i<=m) arr[k++] = arr1[i++];
       while(j<=r) arr[k++] = arr1[j++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        
        if(l==r)
            return;
        int m = l+ (r-l)/2; // prevent overflow condition
        sort(arr,l,m);
        sort(arr,m+1,r);
        merge(arr,l,m,r);
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