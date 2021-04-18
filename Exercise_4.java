// Time Complexity : O(nlogn)
// Space Complexity : O(n) - Extra memory for left array and right array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


class MergeSort
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r)
    {
        int size1 = m - l + 1; // size of first subarray
        int size2 = r - m;     // size of second subarray

        int left[] = new int[size1]; // left subarray
        int right[] = new int[size2]; //right sub array

        for (int i = 0; i < size1; ++i)
            left[i] = arr[l + i];       // copy data to left array
        for (int j = 0; j < size2; ++j)
            right[j] = arr[m + 1 + j];      // copy data to right array


        // Initial indexes of first and second subarrays
        int i = 0, j = 0, k=l;        // intialize pointers for left array right array and merged array

        while (i < size1 && j < size2) { // Compare left and right subarrays
            if (left[i] <= right[j]) {  // if left element less than right 
                arr[k] = left[i];        // rewrite new subarray with smallest value (left element )
                                         //starting from 0 position
                i++;                     // increment left pointer
            }
            else {
                arr[k] = right[j];           // rewrite new subarray with smallest value (right element )
                                             //starting from 0 position
                j++;                       // increment right pointer
            }
            k++;                           // increment merged array pointer
        }


        while (i < size1) {         // Copy remaining elements of left subarray which got missed
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < size2) {         // Copy remaining elements of right subarray which got missed
            arr[k] = right[j];
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

            int m =l+ (r-l)/2;       // Find mid point by avoiding buffer overflow
            sort(arr, l, m);         // sort first subarray
            sort(arr, m + 1, r);     // sort second subarray

            merge(arr, l, m, r);     // merge both arrays
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