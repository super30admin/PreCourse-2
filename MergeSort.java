// Time Complexity : O(NlogN)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
// Traditional merger sort divide and conquer algorithm where in the array is sub divided by a factor of 2 in each iteration till the base case of one element per partition is reached
// after which the array is merger to form the sorted array inplace
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int start, int mid, int end)
    {
        int start2 = mid +1;

        while(start <= mid && start2 <= end){
            if(arr[start] <= arr[start2]){
                start++;
            }else{
                int value = arr[start2];
                int index = start2;
                while(index!= start){
                    arr[index] = arr[index-1];
                    index--;
                }
                arr[start] = value;
                mid++;
                start++;
                start2++;
            }
        }


        //Your code here
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if(l < r){
            int mid = (l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
        }


        //Write your code here
        //Call mergeSort from here
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

