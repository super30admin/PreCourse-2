// Time Complexity : O(n log n), in average case scenario
// Space Complexity : O(n), we are using inbuilt recursion stack
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
        int []temp1 = new int[m-l+1];
        int []temp2 = new int[r - m];

        int n1 = temp1.length;
        int n2 = temp2.length;
        for (int i = 0; i < temp1.length;i++){
            temp1[i] = arr[i];
        }
        for (int j = 0 ;j < temp2.length;j++){
            temp2[j] = arr[m+1+j];
        }

        int i =0;
        int j =0;
        int k = l;
        while (i < n1 && j < n2){
            if (temp1[i] <= temp2[j]){
                arr[k] = temp1[i];
                i++;

            }
            else if(temp1[i] > temp2[j]){
                arr[k] = temp2[j];
                j++;

            }
            k++;
        }
        while (i < n1){
            arr[k] = temp1[i];
            i++;
            k++;
        }
        while (j < n2){
            arr[k] = temp2[j];
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
        if (l < r){
            int mid = (l+r) / 2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
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