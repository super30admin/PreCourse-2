//Time o(n^2) and space o(n)
/// take pivot as last elemet, place pivit such that all elements on left are smaller than pivot and all elemets right to pivot are greater


import java.util.*;
import javafx.util.*;
import java.util.LinkedList;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high)
    {
        //Compare elements and swap.
        while(high > 0 &&low < high){

          if(arr[low] <= arr[high] ){
            low++;
          }
          else{
            int temp = arr[high];
            arr[high] = arr[low];
            arr[low] = arr[high-1];
            arr[high-1] = temp;
            high--;
          }
        }
        return high;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        if(arr == null || arr.length == 0 ) return ;
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        q.add(new Pair<>(l,h));

        while(q.size() > 0 ){
          int size = q.size();
          for( int i =0; i<size; i++){
            Pair<Integer, Integer> curr = q.remove();
            int low = curr.getKey();
            int high = curr.getValue();
            if(low < high){
              int pivot = partition(arr, low, high);
              q.add(new Pair<>(low, pivot-1));
              q.add(new Pair<>(pivot+1, high));
            }
          }

        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n)
    {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[])
    {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}
