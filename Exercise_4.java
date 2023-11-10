// TIME: O(nlogn)
// SPACE: O(n)

// SUCCESS on LeetCode

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
         int mid = m;
         m = m + 1;
        int sortedArr[] = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            sortedArr[i] = arr[i];
        }

        int k = l;
        while (l <= mid && m <= r) {
            if (sortedArr[l] >= sortedArr[m]) {
                arr[k] = sortedArr[m]; 
                m++;
            } else {
                arr[k] = sortedArr[l];
                l++;
            }
            k++;
        }

        while (l <= mid) {
            arr[k] = sortedArr[l];
            k++;
            l++;
        }

        while (m <= r) {
            arr[k] = sortedArr[m];
            k++;
            m++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if ( l < r) {
        int mid = l + (r - l) / 2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
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