// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : Yes, had to look up the solution for iterative quicksort


// Your code here along with comments explaining your approach
// the array is partitioned as in recursive quicksort but a stack is used to keep a track of the boundary indices of the partitions



class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    { // { 4, 3, 5, 2, 1, 3, 2, 3 };
        //Compare elements and swap.
        int pivot = arr[high];
        int i = low-1;
        System.out.println("i "+i+" pivot "+pivot);
        printArr(arr, arr.length);
        for(int j = low;j<=high-1;j++){
            if(arr[j] <= pivot){
                i++;
                swap(arr, i, j);
            }
            System.out.println("i "+i+" pivot "+pivot+" j "+arr[j]);
            printArr(arr, arr.length);
        }
        swap(arr, i+1, high);
        System.out.println("end for loop i "+i+" pivot "+pivot);
        printArr(arr, arr.length);
        return i+1;
    }
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] st = new int[h-l+1];
        int top = -1;
        st[++top] = l;
        st[++top] = h;
        while(top >=0){
            int high = st[top--];
            int low = st[top--];
            int index = partition(arr, low, high);
            if(low < index-1 ){
                st[++top] = low;
                st[++top] = index-1;
            }
            if(index+1 < high){
                st[++top] = index+1;
                st[++top] = high;
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