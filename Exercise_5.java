// Time Complexity : O(n log(n))
// Space Complexity : O(n)
// Did this code successfully run on Leetcode :Not found
// Any problem you faced while coding this : Swap for equal numbers isn't working

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if(arr[i]==arr[j]){
        return;
    }
    System.out.println("i"+arr[i]+"j"+arr[j]);
    arr[j] = arr[i] + arr[j];
    arr[i] = arr[j] - arr[i];
    arr[j] = arr[j] - arr[i];
    System.out.println("afterswap"+"i"+arr[i]+"j"+arr[j]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = (l - 1); // index of smaller element
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or
            // equal to pivot
            if (arr[j] <= pivot) {
                i++;
 
                // swap arr[i] and arr[j]
                swap(arr,i,j);

            }
        }
 
        // swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;
 
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if (l < h) {

            int part = partition(arr, l, h);
 
            // Recursively sort elements before
            // partition and after partition
            QuickSort(arr, l, part - 1);
            QuickSort(arr, part + 1, h);
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