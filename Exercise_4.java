/*
Time Complexity : O(nlogn) => same for best and worse case as we still need to
divide and merge the array.
The division process takes logarithmic time, O(log n) where n is the size of the array.
the merging of two halves takes linear time, i.e., O(n) for each level of recursion,
as each element from both halves is compared and placed in order.

Space Complexity : O(n) => 2 left and right sub arrays are created. They take O(n) space,
where n is the total number of elements in the original array and  In the recursive
implementation, the function calls are added to the call stack.
The depth of the recursion tree is log(n) because the array is divided into two halves
in each step.
*/
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int[] leftSubArr = new int[m-l+1]; // mid index - left index to get the total elements, adding 1 to access the last element
        int[] rightSubArr = new int[r-m];

        //Populate elements in both left and right sub arrays from input array
        for (int i = 0; i < leftSubArr.length; i++) {
            leftSubArr[i] = arr[l + i];
        }

        for (int i = 0; i < rightSubArr.length; i++) {
            rightSubArr[i] = arr[m + 1+ i];
        }

        //Comparing the elements of left sub array to right sub array and adding it in the merge array
        int i = 0, j = 0, k = l;
        while (i < leftSubArr.length && j < rightSubArr.length)
        {
            if(leftSubArr[i] <= rightSubArr[j]) {
                arr[k] = leftSubArr[i];
                i++;
            }
            else {
                arr[k] = rightSubArr[j];
                j++;
            }
            k++;
        }

        //Check for possible elements remaining in either left or right sub arr and add it in input array
        while(i < leftSubArr.length)
        {
            arr[k] =  leftSubArr[i];
            i++;
            k++;
        }
        while(j < rightSubArr.length)
        {
            arr[k] =  rightSubArr[j];
            j++;
            k++;
        }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        // Call mergeSort from here

        int len = r - l + 1; // Calculate the length of the sub array

        /*
            This condition directly checks the length of the sub array.
            If it's less than 2, it means the sub array has only one element or fewer,
            and is already sorted.
         */
        if (len < 2) {
            return;
        }

        int mid = l + (r - l) / 2;

        sort(arr, l, mid);
        sort(arr, mid + 1, r);

        merge(arr, l, mid, r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 