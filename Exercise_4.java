// Time complexity
// O(nlogn)

// Space complexity
// O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
       int leftArr[] = new int[m-l+1];
       int rightArr[] = new int[r-m];

       for (int i = 0; i < leftArr.length; i++) {
        leftArr[i] = arr[l+i];
       }

       for (int i = 0; i < rightArr.length; i++) {
        rightArr[i] = arr[m+1+i];
       }

       int i = 0; int j = 0; int k = l;
       while (i < leftArr.length && j < rightArr.length) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        }
        else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
       }

       while (i < leftArr.length) {
        arr[k] = leftArr[i];
        i++;
        k++;
       }

       while (j < rightArr.length) {
        arr[k] = rightArr[j];
        j++;
        k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if (l < r) {
            int midPoint = (l + r) / 2;
            sort(arr, l, midPoint);
            sort(arr, midPoint + 1, r);
            merge(arr, l, midPoint, r);
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