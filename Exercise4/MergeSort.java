package Exercise4;
// Time Complexity : O(nlogn)
// Space Complexity : O(n), where n is the length of array
// Any problem you faced while coding this : No
class MergeSort
{ 



    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int i = l;  // First subarray is arr[l..m]
        int j = m +1;     // Second subarray is arr[m+1..r]

        // temp array to store sorted elements
        int[] temp = new int[r-l+1];
        int k = 0;

        // Merges two subarrays of arr[].
        while(i < m +1 && j < r + 1) {
            if(arr[i] < arr[j]) {
                temp[k] = arr[i];
                i++;
            } else {
                temp[k] = arr[j];
                j++;
            }
            k++;
        }
        while(i < m +1) {
            temp[k] = arr[i];
            i++;
            k++;
        }
        while(j < r + 1) {
            temp[k] = arr[j];
            j++;
            k++;
        }

        for(i = l; i < r + 1; i++) {
            arr[i] = temp[i-l];
        }
    } 

    void sort(int arr[], int l, int r) 
    {
        if(l < r) {
            int mid = (r - l) / 2 + l;
            // diving the arrays into subarrays
            sort(arr, l , mid);
            sort(arr, mid +1, r);

            // merging the soted array
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