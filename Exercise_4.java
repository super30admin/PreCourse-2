class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r)
    {
        //Your code here
        int ll = m - l + 1;
        int lu = r - m;

        int[] lowerArr = new int[ll];
        int[] upperArr = new int[lu];

        for(int i = 0; i < ll; i++){
            lowerArr[i] = arr[l+i];
        }
        for(int i = 0; i < lu; i++){
            upperArr[i] = arr[m+1+i];
        }

        /* Merge the temp arrays */
        int i = 0, j = 0, k = l;
        while(i < ll && j < lu){
            if(lowerArr[i] < upperArr[j]){
                arr[k++] = lowerArr[i++];
            }else{
                arr[k++] = upperArr[j++];
            }
        }

        // only one of the below two while loops while get executed since the above loop breaks when one of the two
        // pointers (lower array pointer or upper array pointer) reach the end of the array.
        // copy remaining elements from the lower array if any.
        while(i < ll){
            arr[k++] = lowerArr[i++];
        }

        // copy remaining elements from the upper array if any.
        while(j < lu){
            arr[k++] = upperArr[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r)
    {
        //Write your code here
        //Call mergeSort from here
        if(l < r){
            // compute the midpoint of the array.
            int mid = l + (r-l)/2;

            // sort the left half of the array wrt Mid Point.
            sort(arr, l, mid);

            // sort the right half of the array wrt Mid Point.
            sort(arr, mid+1, r);

            // Merge the sorted left half and right half.
            merge(arr, l, mid, r);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String[] args)
    { 
        int[] arr = {12, 11, 13, 5, 6, 7};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 