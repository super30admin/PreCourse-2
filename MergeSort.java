// time complexity 0(nlogn)
// space complexity 0(n)
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    // merge function
    void merge(int arr[], int l, int m, int r) {
        // size of two sub array
        int s1 =m-l+1;
        int s2 = r - m;
        // two temporary array
        int left_sub_array[] = new int[s1];
        int right_sub_array[] = new int[s2];
       // dividing and substituting in temp array
        for(int i=0;i<s1;i++)
            left_sub_array[i] = arr[l + i];
        for(int j=0;j<s2;j++)
            right_sub_array[j] = arr[m + 1 + j];
// comparing from both the temp array and then merging and putting in original array them till i and j move to last
        int i=0, j=0,k=0;
        while(i<s1 && j< s2) {
            if (left_sub_array[i] <= right_sub_array[j]) {
                arr[k] = left_sub_array[i];
                i++;
            }
            else {
                arr[k] = right_sub_array[j];
                j++;
            }
            k++;
        }
        // putting remaining from temp arrat to original array
            while(i<s1)
            {
                arr[k]=left_sub_array[i];
                i++;
                k++;
            }
            while(i<s2)
            {
                arr[k]=right_sub_array[i];
                i++;
                k++;
            }
        }

    // Main function that sorts arr[l..r] using
    // merge()
// if length of list is more than 2 sort the list from left to mid and mid+1 to right and then merge them 
     void sort(int arr[], int l, int r)
    {
        if (l < r) {

            int m=(l+r)/2;


            sort(arr, l, m);
            sort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }

    }




    /* A utility function to print array of size n */


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