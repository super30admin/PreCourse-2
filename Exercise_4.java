// Time Complexity : O(N logN)
// Space Complexity : O(N) + O(logN) I am using a temp array to store the merge result in merge() function, and the logN is recursive call stack
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach



class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // sortedArr is a temp array to hold the sorted elements from the two sub arrays
        int[] sortedArr=new int[r-l+1];
        int currInd=0;
        int i=l, j=m+1;
        while(i<=m && j<=r){
            if(arr[i]<arr[j]){
                sortedArr[currInd]=arr[i];
                i++;
            }else{
                sortedArr[currInd]=arr[j];
                j++;
            }
            currInd++;
        }

        while(i<=m)  sortedArr[currInd++]=arr[i++];
        while(j<=r)  sortedArr[currInd++]=arr[j++];
        for(currInd=0;currInd<sortedArr.length;currInd++) arr[l+currInd]=sortedArr[currInd];
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if(l==r)    return;
        int mid = l + (r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
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
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}