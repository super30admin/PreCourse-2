class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here

        //Calculate the size of 2 sub arrays

        int sizeFirstSubarray = m - l + 1;  //Size of first subarray
        int sizeSecondSubarray = r - m;      //Size of second subarray

        //Create temp array to copy all the data

        int LeftArray[] = new int[sizeFirstSubarray];
        int RightArray[]  = new int[sizeSecondSubarray];

        for (int i=0; i < sizeFirstSubarray; ++i) {
            LeftArray[i] = arr[l+i];
        }

        for (int j=0; j<sizeSecondSubarray; ++j) {
            RightArray[j] = arr[m+1+j];
        }

        //Initialize index to use i & j indexes for comparing values of temp array

        int i = 0, j = 0;

        //Initialize array  index to be copied to after comparing

        int k = l;

        while( i < sizeFirstSubarray && j < sizeSecondSubarray) {

            if (LeftArray[i] <= RightArray[j]) {
                arr[k] = LeftArray[i];
                i++;
            }
            else {

                arr[k] = RightArray[j];
                j++;
            }
            k++;
        }

        //Add  remaining values from Left & Right subarrays if left

        while (i < sizeFirstSubarray) {

            arr[k] = LeftArray[i];
            i++;
            k++;

        }

        while (j < sizeSecondSubarray) {

            arr[k] = RightArray[j];
            j++;
            k++;

        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        if (l < r) {
           int middleElem = l + (r-l) / 2;

           sort(arr,l,middleElem);
           sort(arr,middleElem + 1, r);

            //Call mergeSort from here

            merge(arr,l,middleElem,r);
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