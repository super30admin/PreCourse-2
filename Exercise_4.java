// Time Complexity - O(nlogn)
// Space Complexity - O(n)
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        int half1 = m - l + 1,half2 = r - m,Left[] = new int[half1],Right[] = new int[half2];
        for (int i = 0; i < half1; ++i)
            Left[i] = arr[l + i];
        for (int j = 0; j < half2; ++j)
            Right[j] = arr[m + 1 + j];
        int m1 = 0, m2= 0,k = l;
        while (m1 < half1 && m2< half2) {
            if (Left[m1] <= Right[m2]) {
                arr[k] = Left[m1];
                m1++;
            }
            else {
                arr[k] = Right[m2];
                m2++;
            }
            k++;
        }
        while (m1 < half1) {
            arr[k] = Left[m1];
            m1++;
            k++;
        }
        while (m2 < half2) {
            arr[k] = Right[m2];
            m2++;
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
            int m =l+ (r-l)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
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