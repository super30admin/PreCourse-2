

import java.util.Arrays;
//time complexity O(nlogn) space complexity O(n)
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {  int [] temp= new int[arr.length];
        int count=0;
        int rightStart=m+1;
        int leftStart=l;
        while(l<=m && rightStart<=r){
            if(arr[l]<arr[rightStart]){
                temp[count]=arr[l];
                l++;
            }
            else{
                temp[count]=arr[rightStart];
                rightStart++;
            }
            count++;

        }
        while (l<=m){
            temp[count]=arr[l];
            l++;
            count++;
        }
        while (rightStart<=r){
            temp[count]=arr[rightStart];
            rightStart++;
            count++;
        }
        //System.out.println(Arrays.toString(temp));
        System.arraycopy(temp,0,arr,leftStart,r-leftStart+1);

        //Your code here

    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {if(r>l) {
        int mid = (r + l) / 2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
        merge(arr, l, mid, r);
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