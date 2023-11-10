class MergeSort
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int leftArray[], int rightArray[], int leftSize, int rightSize)
    {
       //Your code here
        int i = 0, j = 0, k = 0;
        while (i < leftSize && j < rightSize) {

            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        while (i < leftSize) {
            arr[k] = leftArray[i];
            k++;
            i++;
        }
        while (j < rightSize) {
            arr[k] = rightArray[j];
            k++;
            j++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[])
    {
	//Write your code here
        //Call mergeSort from here
        // Time Complexity :  o(nlog(n))
        // Space Complexity : 0(n)
        int arrLength = arr.length;
        if (arrLength < 2) {
            return;
        }
        int middle = arrLength / 2;
        int leftArray[] = new int[middle];
        int rightArray[] = new int[arrLength - middle];

        for (int i = 0; i < middle; i++) {
            leftArray[i] = arr[i];
        }
        for (int i = middle; i < arrLength; i++) {
            rightArray[i - middle] = arr[i];
        }

        sort(leftArray);
        sort(rightArray);
        merge(arr, leftArray, rightArray, middle, arrLength - middle);
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
        ob.sort(arr);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 