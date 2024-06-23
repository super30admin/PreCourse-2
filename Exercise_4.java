//Time complexity: O(nlogn) - To Sort array of length n
//Space Complexity: O(n) - Space used to store left and right array values in Temporary Arrays

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftLength = m - l + 1;
        int rightLength = r - m;
        int[] LeftArray = new int[leftLength];
        int[] RightArray = new int[rightLength];
        System.arraycopy(arr, l, LeftArray, 0, leftLength );
        System.arraycopy(arr, m + 1, RightArray, 0, rightLength );
        int leftSortIndex = 0;
        int rightSortIndex = 0;
        int modifyOriginalArrayIndex = l;
        while(leftSortIndex < leftLength && rightSortIndex < rightLength) {
            if(LeftArray[leftSortIndex] <= RightArray[rightSortIndex]) {
                arr[modifyOriginalArrayIndex] = LeftArray[leftSortIndex];
                leftSortIndex++;

            }
            else {
                arr[modifyOriginalArrayIndex] = RightArray[rightSortIndex];
                rightSortIndex++;
            }
            modifyOriginalArrayIndex++;
        }

        while(leftSortIndex < leftLength) {
            arr[modifyOriginalArrayIndex] = LeftArray[leftSortIndex];
            modifyOriginalArrayIndex++;
            leftSortIndex++;
        }
        while(rightSortIndex < rightLength) {
            arr[modifyOriginalArrayIndex] = RightArray[rightSortIndex];
            rightSortIndex++;
            modifyOriginalArrayIndex++;
        }
        printArray(arr);

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if( l < r ) {
            int mid = l + ( r - l)/2;
            sort(arr, l, mid);
            sort (arr, mid + 1, r);

            merge(arr, l, mid, r);

        }
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