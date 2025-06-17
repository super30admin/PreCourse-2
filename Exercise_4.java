// Time Complexity : O(n logn)
// Space Complexity : O(n) - for the new array used in merge(). Recursion - O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) {
        int i = l;
        int j = m + 1;

        int result[] = new int[r - l + 1];
        int k = 0;

        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                result[k] = arr[i];
                ++i;
                ++k;
            } else {
                result[k] = arr[j];
                ++j;
                ++k;
            }
        }
        while (i <= m) {
            result[k] = arr[i];
            ++i;
            ++k;
        }

        while (j <= r) {
            result[k] = arr[j];
            ++j;
            ++k;
        }

        k = 0;

        for(int x = l; x <= r; ++x) {
            arr[x] = result[k++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l >= r) {
            return;
        }
    
        int m = l + (r - l)/ 2;

        sort(arr, l, m);
        sort(arr, m + 1, r);
        merge(arr, l, m, r);

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