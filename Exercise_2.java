/*
Time Complexity :

BEST CASE:
    Quick Sort divides the array like a recursion tree,
    so time taken for a recursion tree = no of levels * time taken for each level

    [n => input size, k => no of levels, we divide n/2^k till we gwt 1
     n/2^k = 1 => n = 2^k => on applying log on both ends  we get,
     log n = k log2(2) {log 2 to base 2 = 1} => log n = k

     So, When the array size is n, recursion tree will have log n levels]

     time taken for a recursion tree = no of levels * time taken for each level
                                     = log n * n
                                     = n log n => O(n log n)

     This is only achieved if the partitions are done, as evenly as possible, so if we choose the best pivot element
     then this can be achieved

WORST CASE:
    The worst case occurs when the pivot chosen is always the smallest or largest element in the array
    eg: when the array is already sorted or reverse sorted, the recursion depth becomes O(n) and O(n) work at each level
    so time complexity = O(n^2)

Space Complexity :
    Best case: O(log n) provided the best pivot is chosen and, it divides the array in half
    Worst case: O(n) due to unbalanced partitions
 */
class QuickSort
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j)
    {
         int temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap

        /*
            Taking the last element as pivot, and here we will be using two pointers which will traverse as we compare it with the pivot
        */
        int pivot = arr[high];
        int leftPointer = low;
        int rightPointer = high;

        while (leftPointer < rightPointer)
        {
            /*
                The first while loop is for checking the left element in the array is less than or equal to pivot
                eg: 1, 90, 87, 6, 110, 100
                    pivot = 100, leftPointer = 0, rightPointer = 4
                    arr[0] = 1
                    1 <= 100 {true} && 0 < 4 {true}
                    leftPointer++ => leftPointer = 1

                The second while loop is for checking the right element in the array is greater than or equal to pivot
                    In above example, pivot = 100, leftPointer = 1, rightPointer = 4
                    arr[4] = 110
                    110 >= 100 {true} && 1 < 4 {true}
                    rightPointer-- => rightPointer = 3
             */
            while (arr[leftPointer] <= pivot && leftPointer < rightPointer)
                leftPointer++;

            while (arr[rightPointer] >= pivot && leftPointer < rightPointer)
                rightPointer--;

            // The check before swapping (if (leftPointer < rightPointer)) prevents unnecessary swaps when the pointers meet
            if (leftPointer < rightPointer) {
                swap(arr, leftPointer, rightPointer);
            }
        }

        // After one iteration with the pivot, it swaps the pivot with the position where leftPointer == rightPointer
        swap(arr, leftPointer, high);

        return leftPointer;
    }

    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
        // Recursively sort elements before
        // partition and after partition

        //If there is just element, we don't need to sort so we just return
        if(low >= high)
            return;

        int leftPointer = partition(arr, low, high);

        /*
         Eg: If we get elements after first complete iteration of pivot,
            original array: 1, 90, 87, 6, 110, 120, 100
            after first iteration: 1, 90, 87, 6, 100, 120, 110
            now all the elements on the left side of the pivot are less than 100 and on the right side are greater than 100,
            so first sort function sort(arr, 0, 3)
            and second sort function sort(arr, 5, 6)
         */
        sort(arr, low, leftPointer - 1);
        sort(arr, leftPointer + 1, high);
    } 
  
    /* A utility function to print array of size n */
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
