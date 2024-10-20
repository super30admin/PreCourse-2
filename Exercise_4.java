// Time Complexity :Best Case: O(n log n)
//                  Average Case: O(n log n)
//                  Worst Case: O(n log n)
// Space Complexity :  O(n), Additional space for the temporary array used during merging.
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : nothing

class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    static void merge(int arr[], int l, int m, int r)
    {
       //Your code here
        int length1=m-l+1;
        int length2= r-m;

        int leftArray[]= new int[length1];
        int rightArray[]= new int[length2];

        for(int i=0; i<length1; ++i){
            leftArray[i]=arr[l+i];
        }
        for(int j=0; j<length2; ++j){
            rightArray[j]=arr[m+1+j];
        }

        int i=0; int j=0; int k=l;

        while(i<length1 && j<length2){
            if(leftArray[i]<=rightArray[j]){
                arr[k]=leftArray[i];
                i++;
            }else{
                arr[k]=rightArray[j];
                j++;
            }
            k++;
        }

        while(i<length1){
            arr[k]=leftArray[i];
            i++;
            k++;
        }
        while(j<length2){
            arr[k]=rightArray[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    static void sort(int arr[], int l, int r)
    {
	//Write your code here
        if(l<r){
            int m= l+(r-l)/2;

            //Call mergeSort from here
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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