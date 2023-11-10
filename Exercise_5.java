// Time Complexity :
//worst case : O(n^2) - since we took the last element as the pivot here, if the pivot is the smallest/largest element of the list. This will happen if the array is already sorted in an ascending/descending order
// n + (n-1) + (n-2) .... 1
//avg case: O(nlogn): time taken by the partition() method for each call will be ~n as we have to traverse through the entire list;
// and assuming that we divide the list in halves in an avg case, it will be log(n)
// n * log(n) = O(nlog(n))
// Space Complexity : since this is a recursive algo, it'll use a stack and the size of the stack will depend on "height" of the tree that will be created after each partition
//which can range from log(n) to n (if the list is already sorted).
// Did this code successfully run on Leetcode :N/A
// Any problem you faced while coding this :
class IterativeQuickSort {

    void swap(int arr[], int i, int j) 
    {
        if(arr[i] != arr[j])
        {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int i = l-1;

        for(int j=l; j < h; j++)
        {
            if(arr[j] <= pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }

        i++;
        swap(arr, i, h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if(arr.length == 0 || l > h)
        {
            return;
        }

        if(l < h)
        {
            int[] stack = new int[arr.length];
            int top = -1;

            //push initial low and high indices on the stack
            stack[++top] = l;
            stack[++top] = h;

            while(top >= 0)
            {
                //pop h and l
                h = stack[top--];
                l = stack[top--];

                int pivotIndex = partition(arr, l, h);

                //sort the left list
                if(pivotIndex-1 > l)
                {
                    stack[++top] = l;
                    stack[++top] = pivotIndex-1;
                }
                //sort the right list
                if(pivotIndex+1 < h)
                {
                    stack[++top] = pivotIndex+1;
                    stack[++top] = h;
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