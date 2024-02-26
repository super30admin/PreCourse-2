// Time Complexity : O(nlogn) since we're dividing the array by half for each operation
// Space Complexity : O(n)
// Any problem you faced while coding this : No
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int n1 = m - l + 1;
        int n2 = r - m;
        int n1_arr[] = new int[n1];
        int n2_arr[] = new int[n2];

        for (int i = 0; i < n1; i++) {
            n1_arr[i] = arr[l + i];
        }

        for (int i = 0; i < n2; i++) {
            n2_arr[i] = arr[m+1+i];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while (i < n1 && j < n2) {
            if (n1_arr[i] <= n2_arr[j]) {
                arr[k] = n1_arr[i];
                i++;
            } else {
                arr[k] = n2_arr[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = n1_arr[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = n2_arr[j];
            j++;
            k++;
        }

       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if (l < r) {
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
            merge(arr, l, m, r);
        }
	//Write your code here
        //Call mergeSort from here 
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