class MergeSort
{
    // Time Complexity : O(nLogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void conquer(int left[], int right[], int arr[] ){
        int nLeft = left.length;
        int nRight = right.length;
        int i=0;
        int j=0;
        int k=0;
        while (i<nLeft && j<nRight){
            if(left[i]<=right[j]){
                arr[k] = left[i];
                k++;
                i++;
            }
            else{
                arr[k] = right[j];
                k++;
                j++;
            }
        }
        while (i<nLeft){
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j<nRight){
            arr[k] = right[j];
            j++;
            k++;
        }

    }


    // Main function that sorts arr[l..r] using
    // merge()
    void divide(int arr[])
    {
        //Write your code here
        //Call mergeSort from here
        int n = arr.length;
        if (n<2) return;
        int mid = n/2;
        int left[] = new int[mid];
        int right[] = new int[n-mid];
        for (int i = 0;i<=mid-1;i++){
            left[i]=arr[i];
        }
        for (int i = mid;i<=n-1;i++){
            right[i-mid]=arr[i];
        }
        divide(left);
        divide(right);
        conquer(left,right,arr);
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
        ob.divide(arr);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 