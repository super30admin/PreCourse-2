/*
        Time Complexity: O(NLongN)
        Space Complexity: O(N) for the extra array
 */
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        /*
         2, 34, 45, 1, 35, 67

         temp1 = 2
         temp2 = 1


         */
       //Your code here

        int length = r-l+1;

        int input[] = new int[length];

        int first = l;
        int second = m+1;
        int index = 0;

        while(first <= m || second <= r) {

            if(first <= m && second <= r) {
                if(arr[first] < arr[second]) {
                    input[index] = arr[first++];
                } else {
                    input[index] = arr[second++];
                }
            } else if(first <= m) {
                input[index] = arr[first++];
            } else {
                input[index] = arr[second++];
            }
            index++;
        }

        for(int i =l ;i <= r; i++) {
            arr[i] = input[i-l];
        }

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        printArray(arr);
	    //Write your code here
        //Call mergeSort from here

        if(l>=r) {
            return;
        }

        int mid = (l+r)/2;

        sort(arr, l, mid);
        sort(arr, mid+1, r);

        merge(arr, l, mid, r);
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
