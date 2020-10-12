class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int lsize=m-l+1, rsize=r-m;
       //Your code here  
       int left[] = new int[lsize];
       int right[] = new int[rsize];

       for (int i = 0; i < lsize; ++i) 
            left[i] = arr[l + i]; 
        for (int j = 0; j < rsize; ++j) 
            right[j] = arr[m + 1 + j]; 
  
     
        int i = 0, j = 0; 
        int k = l; 
        while (i < lsize && j < rsize) { 
            if (left[i] <= right[j]) { 
                arr[k] = left[i]; 
                i++; 
            } 
            else { 
                arr[k] = right[j]; 
                j++; 
            } 
            k++; 
        } 
  
        while (i < lsize) { 
            arr[k] = left[i]; 
            i++; 
            k++; 
        } 
  
        while (j < rsize) { 
            arr[k] = right[j]; 
            j++; 
            k++; 
        } 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l<r) {
            int mid = (l+r)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr, l, mid, r);
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