class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int left_count = m - l + 1;
        int right_count = r - m;
 
        int left[] = new int[left_count];
        int right[] = new int[right_count];
 
        for (int i = 0; i < left_count; ++i)
            left[i] = arr[l + i];
        for (int j = 0; j < right_count; ++j)
            right[j] = arr[m + 1 + j];
 
        int i = 0;
	int j = 0;
        int k = l;
	    
        while (i < left_count && j < right_count) {
            if (left[i] > right[j]) {
		arr[k] = right[j++];
            }else {
		 arr[k] = left[i++];
            }
            k++;
        }
 
        while (i < left_count) {
            arr[k] = left[i];
            i++; k++;
        }
 
        while (j < right_count) {
            arr[k] = right[j];
            j++; k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l < r) {
            int m =l+ (r-l)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
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
