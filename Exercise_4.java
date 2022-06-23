class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftcount = m - l + 1;
        int rightcount = r - m;

        int LeftArray[] = new int[leftcount];
        int RightArray[] = new int[rightcount];

        /*Copy data to temp arrays*/
        for (int i = 0; i < leftcount; ++i)
            LeftArray[i] = arr[l + i];
        for (int j = 0; j < rightcount; ++j)
            RightArray[j] = arr[m + 1 + j];

        /* Merge the temp arrays */

        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarray array
        int k = l;
        while (i < leftcount && j < rightcount) {
            if (LeftArray[i] <= RightArray[j]) {
                arr[k] = LeftArray[i];
                i++;
            }
            else {
                arr[k] = RightArray[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < leftcount) {
            arr[k] = LeftArray[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < rightcount) {
            arr[k] = RightArray[j];
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
        if (l < r) {
            // Find the middle point
            int middleindex =l+ (r-l)/2;

            // Sort first and second halves
            sort(arr, l, middleindex);
            sort(arr, middleindex + 1, r);

            // Merge the sorted halves
            merge(arr, l, middleindex, r);
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