class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int[] left = new int[m];

        for (int i=0; i<m; i++) {
            left[i] = arr[i];
        }

        int[] right = new int[arr.length - m];

        for (int i=m; i<arr.length; i++) {
            right[i - m] = arr[i];
        }

        int i=0;
        int j=0;
        int k=0;

        while (i < left.length && j<right.length) {

            if (left[i] <= right[i]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }

        }

        while (i<left.length) {
            arr[k++] = left[i++];
        }

        while (j<right.length) {
            arr[k++] = right[j++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r)
    { 
	//Write your code here
        //Call mergeSort from here
        if (arr.length < 2) {
            return;
        }

        if (r > l) {
            return;
        }

        int mid = arr.length / 2;

        sort(arr, l, mid);
        sort(arr, mid + 1, r);

        merge(arr, l, mid, r);
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