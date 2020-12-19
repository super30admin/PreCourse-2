// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        // get size of subarrays
        int arrSize1 = m - l + 1;
        int arrSize2 = r - m;

        //Create temp arrays
        int temp1[] = new int[arrSize1];
        int temp2[] = new int[arrSize2];

        //Copy data to temp arrays
        for (int i = 0; i < arrSize1; ++i)
            temp1[i] = arr[l + i];
        for (int j = 0; j < arrSize2; ++j)
            temp2[j] = arr[m + 1 + j];

        int i = 0, j = 0;

        // merge subarrays
        int k = l;
        while (i < arrSize1 && j < arrSize2) {
            if (temp1[i] <= temp2[j]) {
                arr[k] = temp1[i];
                i++;
            }
            else {
                arr[k] = temp2[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of temp1
        while (i < arrSize1) {
            arr[k] = temp1[i];
            i++;
            k++;
        }

        // Copy remaining elements of temp2
        while (j < arrSize2) {
            arr[k] = temp2[j];
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
            // Find mid point
            int m = (l + r) / 2;

            // Sort first half
            sort(arr, l, m);

            //sort second half
            sort(arr, m + 1, r);

            // Merge both halves
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