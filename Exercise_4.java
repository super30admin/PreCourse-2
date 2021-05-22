// Time Complexity : O(NlogN)
// Space Complexity : O(N)
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

       //Lengths of first and second sub arrays
       int firstSubArrayLength = m - l + 1;
       int secondSubArrayLength = r - m;

       int[] firstSubArray = new int[firstSubArrayLength];
       int[] secondSubArray = new int[secondSubArrayLength];

       //filling first subarray
       for(int i = 0; i < firstSubArrayLength; i++){
         firstSubArray[i] = arr[l + i];
       }
       //filling second subarray
       for(int i = 0; i < secondSubArrayLength; i++){
         secondSubArray[i] = arr[m + 1 + i];
       }

       int i =0, j = 0, k = l;

       //Merging the two subarrays
       while(i < firstSubArrayLength && j < secondSubArrayLength){
         if(firstSubArray[i] <= secondSubArray[j]){
           arr[k] = firstSubArray[i];
           i++;
         }else{
           arr[k] = secondSubArray[j];
           j++;
         }
         k++;
       }
       //checking for any remaining elements in first subarray
       while(i < firstSubArrayLength){
         arr[k] = firstSubArray[i];
         i++;
         k++;
       }
       //checking for any remaining elements in second subarray
       while(j < secondSubArrayLength){
         arr[k] = secondSubArray[j];
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

        if(l < r){
          int mid = (l + r)/2;

          sort(arr, l, mid);
          sort(arr, mid + 1, r);

          merge(arr, l, mid, r);
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
