

// Time Complexity : O(nlogn)
// Space Complexity : O(n)


package S30_Codes.PreCourse_2;

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int i = l;
        int j = m+1;
        int tempArr[] = new int[r-l+1];
        int tempIdx = 0;

        // returns true until one subarray is not completed
        while (i<=m && j<=r){
            if(arr[i] <= arr[j])
                tempArr[tempIdx++] = arr[i++];
            else
                tempArr[tempIdx++] = arr[j++];
        }

        // if First subarray is not completed
        while (i <= m){
            tempArr[tempIdx++] = arr[i++];
        }

        // if Second subarray is not completed
        while (j <= r){
            tempArr[tempIdx++] = arr[j++];
        }

        // replacing sorted tempArray to original array
        tempIdx = 0;
        for (int k=l; k<=r; k++){
            arr[k] = tempArr[tempIdx++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if(l < r) {
            int m = (l + r) / 2;
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