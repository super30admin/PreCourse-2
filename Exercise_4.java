// Time Complexity : O(n logn)
// Space Complexity : O(log n)
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
//find sizes of the two sub-arrays
        int sizeFirst = m - l + 1;
        int sizeLater = r - m;

        int[] L = new int[sizeFirst];
        int[] R = new int[sizeLater];
//populate two working sub-arrays
        for(int x=0; x<sizeFirst; x++){
            L[x] = arr[l+x];
        }
        for(int y=0; y<sizeLater; y++){
            R[y] = arr[m+1+y];
        }
//populating sorted items into arr
        int i=0, j=0;
        int k=l; //uses current low which is not necessarily 0
        while(i<sizeFirst && j<sizeLater){
            if(L[i] < R[j]) {
                arr[k] = L[i];
                i++;
            }else{
                arr[k] = R[j];
                j++;
            } k++;
        }
        while(i<sizeFirst){
            arr[k] = L[i];
            i++; k++;
        }
        while(j<sizeLater){
            arr[k] = R[j];
            j++; k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        //Call mergeSort from here
        if(l<r){
            int mid = l + ( (r-l)/2 );
            // sort first & second halves
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            // merge sorted halves
            merge(arr, l, mid,r);
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