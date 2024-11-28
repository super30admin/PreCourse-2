// Time Complexity: O(nlogn)
// Space Complexity: O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //Your code here

        int left_length = m - l + 1;
        int right_length = r - m;

        int[] left = new int[left_length];
        int[] right = new int[right_length];

        // construct the left and right array
        for (int i=0;i<left_length;i++) {
            left[i] = arr[l+i];
        }

        for(int j=0;j<right_length;j++) {
            right[j] = arr[j + m  + 1];
        }

        // Merge the two aubarrays and modify the original Array
        int a = 0;
        int b = 0;

        int k = l;

        while (a < left_length && b < right_length) {
            if (left[a] <= right[b]) {
                arr[k] = left[a];
                a++;
                k++;
            } else {
                arr[k] = right[b];
                b++;
                k++;
            }
        }

        while (a < left_length) {
            arr[k++] = left[a++];
        }

        while (b < right_length) {
            arr[k++] = right[b++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here

        // Base case
        // if there is only one element, array is considered sorted
        if (r-l < 1) {
            return;
        }

        //Call mergeSort from here

        // Divide the array into two halves
        int mid = l + (r - l)/2;

        // Call sort function recursively for left and right array
        sort(arr, l, mid);
        sort(arr, mid+1, r);

        // Call merge function to merge the left and right array into original array
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