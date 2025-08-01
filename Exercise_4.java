class MergeSort {
// Time Complexity : O(nlogn) all cases
// Space Complexity : O(logn) recursive stack space
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        // 
        int n1 = m - l + 1;
        int n2 = r - m;
        int arrIndex = l;

        // Create 2 subarrays
        int[] leftArr = new int[n1];
        int[] rightArr = new int[n2];

        // Fill sub array
        for(int i = 0; i < n1; i++)
            leftArr[i] = arr[arrIndex++];
        
        for(int j = 0; j < n2; j++)
            rightArr[j] = arr[arrIndex++];

        // merge and sort
        int i = 0;
        int j = 0;
        int k = l;
        while(i < n1 && j < n2){
            if(leftArr[i] <= rightArr[j]){
                arr[k] = leftArr[i];
                i++;
            }
            else {
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while(i < n1){
            arr[k] = leftArr[i];
            i++;
            k++;
        }

        while(j < n2){
            arr[k] = rightArr[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if (l == r) {
            return;
        }
        int mid = l + (r - l) / 2;
        // seperate left and right side
        sort(arr, l, mid); // split left
        sort(arr, mid + 1, r); // split right
        // merge and sort while g back
        merge(arr, l, mid, r);
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 9, 8, 7, 6, 5, 4, 3, 2, 1 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}