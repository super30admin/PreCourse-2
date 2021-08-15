

// Time Complexity: Best O(n log n)
// Space Complexity: O(log n)
// Did this code successfully run on Leetcode:
//Any problems you faced while coding this:



class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int[] arr, int l, int m, int r)
    {
        int l1 = m - l +1;
        int r1 = r-m;

        int[] arr1 = new int[l1];
        int[] arr2 = new int[r1];

        for (int q = 0; q < l1; q++){
            arr1[q] = arr[q + l];
        }

        for (int w = 0; w < r1; w++){
            arr2[w] = arr[m + 1 + w];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while(i<l1 && j<r1){
            if(arr1[i] <= arr2[j]){
                arr[k] = arr1[i];
                i++;
            }
            else{
                arr[k] = arr2[j];
                j++;
            }
            k++;
        }
        while (i<l1){
            arr[k] = arr1[i];
            i++;
            k++;
        }
        while (j<r1){
            arr[k]  = arr2[j];
            j++;
            k++;

        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if (l<r) {
            int q = l + (r - l) / 2;
            sort(arr, l, q);
            sort(arr, q + 1, r);
            merge(arr, l, q, r);
        }
	//Write your code here
        //Call mergeSort from here
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