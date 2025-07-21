// Time Complexity : O(n logn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        int[] tmp = new int[r-l+1];
        int ptr1 = l;
        int ptr2 = m+1;
        int tmpPtr = 0;
        while(ptr1 <= m && ptr2 <= r) {
            if (arr[ptr1] > arr[ptr2]) {
                tmp[tmpPtr++] = arr[ptr2];
                ptr2++;
            } else if (arr[ptr1] < arr[ptr2]) {
                tmp[tmpPtr++] = arr[ptr1];
                ptr1++;
            } else {
                tmp[tmpPtr++] = arr[ptr1];
                tmp[tmpPtr++] = arr[ptr2];
                ptr1++;
                ptr2++;
            }
        }

        while(ptr1 <= m) {
            tmp[tmpPtr++] = arr[ptr1];
            ptr1++;
        }
        while(ptr2 <= r) {
            tmp[tmpPtr++] = arr[ptr2];
            ptr2++;
        }

        //copy from tmp to arr
        int k=0;
        for(int i=l; i <= r; i++) {
            arr[i] = tmp[k++];
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here
        if(l == r) {
            return;
        }
        int m = l + ((r - l)/2);
        // divide left
        sort(arr, l, m);
        // divide right
        sort(arr, m+1, r);
        // merge
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