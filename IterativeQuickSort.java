// Time Complexity :O(NlogN)
// Space Complexity : O(1) we are sorting inplace here
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
// Taking the first element as the pivot and arranging the other
// elements w.r.t to that pivot and then recursively applying the quick sort to the two seperate portins of the array
// Only different is that instead of calling the sort function recursively, I am using external stacks which store the lower bound and upper bound of the array to be sorted.
import java.util.Arrays;
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        //Try swapping without extra variable
    }
    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int low, int high)
    {
        int pivot = low;
        while(low < high){
            while(low < arr.length-1 && arr[low] <= arr[pivot] ){
                low++;
            }
            while(high > 0 && arr[high] > arr[pivot]){
                high--;
            }
            System.out.println(low+" "+high);
            if (low<high){
                swap(arr,high,low);
                System.out.println("swap");
            }
        }
        swap(arr,high,pivot);
        Arrays.stream(arr).forEach(System.out::print);
        System.out.println();
        return high;
        //Compare elements and swap.
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int low, int high)
    {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        s1.push(low);
        s2.push(high);
        while(!s1.isEmpty()){
            int l = s1.pop();
            int h = s2.pop();
            if(l<h){
                int p = partition(arr,l,h);
                s1.push(l);
                s2.push(p-1);
                s1.push(p+1);
                s2.push(h);
            }
        }

        //Try using Stack Data Structure to remove recursion.
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
