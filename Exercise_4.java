/* Algorithm: Merge Sort
 * 1. Recursively divide the given array into half
 *      1.1 Find mid 
 *      1.2 Recursively divide left array
 *      1.3 Recursively divide right array
 * 2. Merge and Sort Sub Arrays
 *      2.1 Create temp arrays to store left and right elements
 *      2.2 Copy elements from left and right to temp arrays
 *      2.3 If left-array element < right-array element --> replace k element in original array with left element, vice-versa
 *      2.4 Copy remaining elements to the original array from un-exhausted array 
 * 
 * Time Complexity: O(n log n)
*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int left, int mid, int right) 
    {  
        //Sizes of left and right arrays
       int leftArrayLength = mid - left + 1;
       int rightArrayLength = right - mid;

       //Create temp arrays to store left and right elements
       int leftArray[] = new int[leftArrayLength];
       int rightArray[] = new int[rightArrayLength];

       //Copy elements from left and right to temp arrays
       for(int i = 0; i < leftArrayLength; ++i)
       {
            leftArray[i] = arr[left + i];
       }
       for(int j = 0; j < rightArrayLength; ++j)
       {
            rightArray[j] = arr[mid + 1 + j];
       }

       //**Merge-Sort Logic**
       //Pointers to hold indexes of original array and left and right array
       int i = 0, j = 0;  
       int k = left;

       while(i < leftArrayLength && j < rightArrayLength)
       {
            if(leftArray[i] <= rightArray[j])
            {
                arr[k] = leftArray[i];
                i++;
            }
            else
            {
                arr[k] = rightArray[j];
                j++;
            }
            
            k++; // Increment original arrays index
       }

       //One of the array will exhaust at this point and another one will have elements
       //Copy remaining elements to the original array
       while(i < leftArrayLength)
       {
            arr[k] = leftArray[i];
            i++;
            k++;
       }
       while(j < rightArrayLength)
       {
            arr[k] = rightArray[j];
            j++;
            k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int left, int right) 
    { 
       
	    // Recursively divide the given array into half
       if(left < right)
       {
            //Find mid 
            int mid = left + (right - left)/2;

            //Recursively divide left array
            sort(arr, left, mid);
            //Recursively divide right array
            sort(arr, mid+1, right);
            //Recursively Merge both the parts
            merge(arr, left, mid, right);
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