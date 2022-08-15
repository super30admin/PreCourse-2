/* /*******
Exercise_2 : Quick sort.

Time Complexity :                               O(n logn)
Space Complexity :                              O(n)  
Did this code successfully run on Leetcode :    No (Could not find on Leetcode)
Any problem you faced while coding this :       Yes

Problem - swapping without extra variable 
    Logic:
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];

    Output:
        Before: 3 3
        After: 0 0

    Why the output is 0 0 ?

****/

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    {
	    //swapping without extra variable 
        // arr[i] = arr[i] + arr[j];
        // arr[j] = arr[i] - arr[j];
        // arr[i] = arr[i] - arr[j];

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
        int pIndex = low;

        for ( int i = low ; i < high; i++ ){
            if ( arr[i] <= pivot ){
                swap(arr, i, pIndex);
                pIndex++;
            }
        }
        swap(arr, pIndex, high);
        return pIndex;
    } 
  
    // Sorts arr[low..high] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
        //Using Stack Data Structure to remove recursion.
        int[] stack = new int[high - low + 1];

        int top = -1;

        stack[++top] = low;
        stack[++top] = high;

        while( top >= 0){

            high = stack[top--];
            low = stack[top--];

            int pIndex = partition(arr, low, high);

            if ( pIndex - 1 > low){
                stack[++top] = low;
                stack[++top] = pIndex - 1;
            }
            if ( pIndex + 1 < high){
                stack[++top] = pIndex + 1;
                stack[++top] = high;
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