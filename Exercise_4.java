// Time Complexity : O(NLOGN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        //Your code here
        int size1 = m - l + 1;
        int size2 = r - m;

        int leftarr[] = new int[size1];
        int rightarr[] = new int[size2];

        for (int i = 0; i < size1; i++)
            leftarr[i] = arr[l + i];
        for (int j = 0; j < size2; j++)
            rightarr[j] = arr[m + 1 + j];


        int i = 0, j = 0;
        int k = l;

        while (i < size1 && j < size2) {
            if (leftarr[i] < rightarr[j]) {
                arr[k] = leftarr[i];
                i++;
            } else {
                arr[k] = rightarr[j];
                j++;
            }
            k++;
        }

        while (i < size1){
            arr[k]=leftarr[i];
            i++;
            k++;
        }
        while (j < size2) {
            arr[k] = rightarr[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int left, int right)
    {
        if(left<right)
        {
            int mid = left + ((right-left)/2);
            sort(arr,left,mid);
            sort(arr,mid+1,right);
            merge(arr,left,mid,right);
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
