// Time Complexity  :    O(nlogn)
// Space Complexity :    O(n)
//  Yes, It's run successfully
// No I don't face any problem.


class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
        int len1 = m - l + 1;
        int len2 = r - m;

        //made two small array and assign values from the main array
        int[] arr1 = new int[len1];
        int[] arr2 = new int[len2];

        for(int i=0; i<len1; i++){
            arr1[i] = arr[l+i];
        }

        for (int i=0; i<len2; i++){
            arr2[i] = arr[m+i+1];
        }

        int i=0;
        int j=0;
        int k=l;
        // use 2 pointer to sort two arrays and put values in a main array in a sorted manner
        while (i<len1 && j< len2){

            if(arr1[i]<arr2[j]){
                arr[k]=arr1[i];
                k++;
                i++;
            }
            else {
                arr[k]=arr2[j];
                j++;
                k++;
            }
        }
        //put remaining elements of 1st array into main array
        while (i<len1){
            arr[k]=arr1[i];
            i++;
            k++;

        }
        //put remaining elements of 2nd array into main array
        while (j<len2){
            arr[k]=arr2[j];
            j++;
            k++;

        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        if (l<r){

            int q=(l+r)/2; //midpoint
            sort(arr, l, q); //divide the array into 2 halves
            sort(arr, q+1, r);

            //Call mergeSort from here
            merge(arr, l, q, r); // merge two arrays
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