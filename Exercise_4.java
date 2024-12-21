// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
class MergeSort
{
    /*
    Function divides the array into mid and compares every ele in forst half with second. It then copies the remaining eles
    Time complexity wise Merge sort > Quick sort as in worst case quick can be O(N2) but merge is always O(NLOGN)
    Space complexity quick is better as merge requires a whole new array to be created
    @params : arr, left index, mid index, right index
    @return none
     */
    void merge(int arr[], int l, int m, int r)
    {
       int i = l;
       int j = m+1;
       int k =l;
       int [] brr = new int[arr.length];
       while (i<=m && j<=r){
           if(arr[i]<arr[j]){
               brr[k] = arr[i];
               i++;
           } else {
               brr[k] = arr[j];
               j++;
           }
           k++;
       }
       while (i<=m){
           brr[k] = arr[i];
           k++;i++;
       }
        while (j<=r){
            brr[k] = arr[j];
            k++;j++;
        }
        for(int n=l;n<=r;n++){
            arr[n]=brr[n];
        }
    }
    /*
    finds every mid and recursively calls left to mid and mid+1 to right then merges it
    @param: arr, left index, right index
    @return none
     */
    void sort(int arr[], int l, int r)
    {
	    if(l<r){
            int mid = (l+r)/2;
            sort(arr, l, mid);
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