// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Had to revisit the Iterative QuickSort algorithm.
import java.util.*;

class IterativeQuickSort {
  void swap(int arr[], int i, int j)
  {
    //Try swapping without extra variable
    if(i!=j){
      arr[i] = arr[i] + arr[j];
      arr[j] = arr[i] - arr[j];
      arr[i] = arr[i] - arr[j];
    }
  }

  /* This function is same in both iterative and
  recursive*/
  int partition(int arr[], int l, int h)
  {
    //Compare elements and swap.
    int pivotElement = arr[h];

    int partitionIndex = l;

    for(int i = l; i < h; i++){
      if(arr[i] <= pivotElement){
        //swap
        swap(arr, partitionIndex, i);
        partitionIndex++;
      }
    }
    swap(arr, partitionIndex, h);
    return partitionIndex;
  }

  // Sorts arr[l..h] using iterative QuickSort
  void QuickSort(int arr[], int l, int h)
  {
    //Try using Stack Data Structure to remove recursion.
    Stack<Integer> stack = new Stack<>();
    stack.push(l);
    stack.push(h);

    while(!stack.isEmpty()){
      h = stack.pop();
      l= stack.pop();

      int partitionIndex = partition(arr, l , h);

      if(partitionIndex -1 > l){
        stack.push(l);
        stack.push(partitionIndex-1);
      }

      if(partitionIndex +1 < h){
        stack.push(partitionIndex+1);
        stack.push(h);
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
