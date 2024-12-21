// Time Complexity : O(nlogn)
// Space Complexity : O(n) where n is length of array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : On leetcode got TLE error but when choosing pivot as a random number when array is sorted or almost sorted Time complexity becomes O(N2)

import java.util.Random;

class QuickSort
{
    /*
        Swaps any two numbers at i and j index in arr
        @param:arr, i, j
        @return none
     */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    /*
    Returns the pivot index which is finally in its sorted pos. Everything before and after is unsorted.
    @params: arr, low, high
    @return: pivot index
     */
    int partition(int arr[], int low, int high)
    {
        Random rand = new Random();
        int pivotIndex = low + rand.nextInt(high - low + 1);
        swap(arr, pivotIndex, high);
        int i = low-1;
           for(int j = low;j<high;j++){
               if(arr[j]<arr[high]){
                   i++;
                   swap(arr,i,j);
               }
           }
           swap(arr,i+1,high);
           return i+1;
    }

    /*
    Recursive call for elements before and after pivot index
    @params: arr, low, high
    @return: None
     */
    void sort(int arr[], int low, int high)
    {
            if(low<high){
                int pivotIndex = partition(arr,low,high);
                sort(arr,low,pivotIndex-1);
                sort(arr,pivotIndex+1, high);
            }
    }

    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[])
    {
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
