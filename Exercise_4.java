class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int c1 = l, c2 = m+1, c3 = l;
       int[] B = new int[arr.length];

        for(int i=0; i<arr.length; i++) {
            B[i] = arr[i];
        }

        while(c1 <= m && c2 <= r)
        {
            if(B[c1] < B[c2])
            {
                arr[c3] = B[c1];
                c1++;
                c3++;
            }
            else
            {
                arr[c3] = B[c2];
                c2++;
                c3++;
            }
        }
        while( c1 <= m )
        {
            arr[c3] = B[c1];
            c1++;
            c3++;
        }
        while( c2 <= r )
        {
            arr[c3] = B[c2];
            c2++;
            c3++;
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
            int mid = (l + r) / 2;
            sort( arr, l, mid );
            sort( arr, mid+1, r );
            merge( arr, l, mid, r );
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