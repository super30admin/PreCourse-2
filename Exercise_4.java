class MergeSort { 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {  
        int n1 = m - l + 1; // Size of first half
        int n2 = r - m;     // Size of second half

        // Create temporary arrays for the two halves
        int left[] = new int[n1];
        int right[] = new int[n2];

        // Copy data to temp arrays
        for (int i = 0; i < n1; i++)
            left[i] = arr[l + i];
        for (int j = 0; j < n2; j++)
            right[j] = arr[m + 1 + j];

        // Merge the temporary arrays back into arr[l..r]
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy any remaining elements of left[]
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy any remaining elements of right[]
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using merge()
    void sort(int arr[], int l, int h) { 
        int mid, p, i;
        // Loop for different sizes of subarrays to merge (1, 2, 4, 8, ...)
        for (p = 2; p <= arr.length; p = p * 2) {
            // Merge subarrays in pairs
            for (i = 0; i + p - 1 < arr.length; i += p) {
                l = i;
                h = i + p - 1;
                mid = (l + h) / 2;
                merge(arr, l, mid, h);
            }
        }
        
        // If array size is not a power of 2, merge remaining part
        if (p / 2 < arr.length) {
            merge(arr, 0, p / 2 - 1, arr.length - 1);
        }
    }
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) { 
        int n = arr.length; 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    }
  
    // Driver method 
    public static void main(String args[]) { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
        System.out.println("Given Array"); 
        printArray(arr);
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length - 1);
  
        System.out.println("\nSorted array"); 
        printArray(arr);
    } 
} 
