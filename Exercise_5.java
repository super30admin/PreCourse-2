// Time Complexity : O(nlogn)
// Space Complexity : O(n) where n is length of array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Identifying the iterative approach using stack
import java.util.Random;
import java.util.Stack;

class IterativeQuickSort {
    /*
        Swaps any two numbers at i and j index in arr
        @param:arr, i, j
        @return none
     */
    void swap(int arr[], int i, int j)
    {
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    /*
   Returns the pivot index which is finally in its sorted pos. Everything before and after is unsorted.
   @params: arr, low, high
   @return: pivot index
    */
    int partition(int arr[], int l, int h)
    {
        Random rand = new Random();
        int pivot = l+rand.nextInt(h-l+1);
        swap(arr,pivot,h);
        int i=l-1;
        for(int j=l;j<h;j++){
            if(arr[j]<arr[h]){
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return  i+1;
    }
    /*
   Stack is used that mainatins h,l, p+1 and p-1 and pops the upper bound and lower bound and passes it.
    @params: arr, low, high
    @return: None
     */
    void QuickSort(int arr[], int l, int h)
    {
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

         while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();
            int pivotIndex = partition(arr, l, h);
            if(pivotIndex-1>l){
                stack.push(l);
                stack.push(pivotIndex-1);
            }
             if(pivotIndex+1<h){
                 stack.push(pivotIndex+1);
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