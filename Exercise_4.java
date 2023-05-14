class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //Your code here  
        int[] left = new int[m-l+1];
        int[] right = new int[r-m];
        for (int i=0; i<left.length; i++)
        {
            left[i] = arr[l+i];
        }
        for (int i=0; i<right.length; i++)
        {
            right[i] = arr[m+i+1];
        }
        int i=0, j=0, index=l;
        while(i<left.length&&j<right.length)
        {
            if (left[i]<=right[j])
            {
                arr[index++] = left[i++];
            }
            else
            {
                arr[index++] = right[j++];
            }
        }
        while(i<left.length)
        {
            arr[index++] = left[i++];
        }
        while(j<right.length)
        {
            arr[index++] = right[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        //Call mergeSort from here
        if (l<r)
        {
            int m = l+(r-l)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
            merge(arr, l, m, r);
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