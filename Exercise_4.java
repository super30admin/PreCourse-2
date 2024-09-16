//TC : Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best)
// as merge sort always divides the array into two halves and takes linear time to merge two halves.
//SC : O(n) requires equal amount of space as the sorted array
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {

        //find the length of the two halves to be merged
        int n1 = m-1+1;
        int n2= r-m;

        //create temp arrays
        int[] left = new int[n1];
        int[] right = new int[n2];

        //copy the data to the temp arrays
        for (int i = 0; i < n1; ++i)
            left[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            right[j] = arr[m + 1 + j];

        //index of merged array
        int i = 0, j = 0;

        // Initial index of merged array
        int k = l;
        while (i < n1 && j < n2)
        {
            if (left[i] <= right[j])
            {
                arr[k] = left[i];
                i++;
            }
            else
            {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        //copy the remaining elements of the arrays if any
        while (i < n1)
        {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < n2)
        {
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
        if(l<r)
        {
            int middle = (r-l)/2 +l;

            // sort the two halves
            sort(arr,l,middle);
            sort(arr,middle+1,r);

            //merge the two sorted halves
            merge(arr,l,middle,r);
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