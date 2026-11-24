// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : No
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int[] merged = new int[r - l + 1];
        int left = l;
        int right = m + 1;
        int index = 0;

        while (left <= m && right <= r) {
            if (arr[left] <= arr[right]) {
                merged[index++] = arr[left++];
            } else {
                merged[index++] = arr[right++];
            }
        }

        while (left <= m) {
            merged[index++] = arr[left++];
        }

        while (right <= r) {
            merged[index++] = arr[right++];
        }

        for (int i = 0; i < merged.length; i++) {
            arr[l + i] = merged[i];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if (l >= r) {
            return;
        }

        int m = l + (r - l) / 2;

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