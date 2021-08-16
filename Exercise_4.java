//Time complexity: O(n logn)
//Space complexity: O(n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int n = m - l + 1;
        int n2 = r - m;

        //Create temporary arrays
        int L[] = new int[n];
        int R[] = new int[n2];

        //This loops will copy the elements of left subarray to left tmp array and right subarray to right tmp array.
        for (int i = 0; i < n; i++) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        //Initialize the index of two subarrays
        int i = 0, j = 0;

        int k = l;
        while (i < n && j < n2) {
            //If the element in the left sub array is less than or equal to the element in the right array, it will be added to the array
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            //If the element in the left sub array is greater than the element in the right array, it will be added to the array
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        //This will copy the remaining elements of left sub array
        while (i < n) {
            arr[k] = L[i];
            i++;
            k++;
        }

        //This will copy the remaining elements of right sub array
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(r > l) {
            int mid = l + (r-l)/2;

            //divide the arr into two halves
            sort(arr, l, mid - 1);
            sort(arr, mid + 1, r);

            //Call mergeSort from here
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