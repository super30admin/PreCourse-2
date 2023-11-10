// Time Complexity : O(NlogN) where N is the number of elements in the list
// Space Complexity : O(N) since using temp array to store the elements
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None


// Your code here along with comments explaining your approach

/**
 * @author akhilreddy619
 * Initially, we find a mid index and apply merge sort recursively on two halves of mid
 * (l, mid), (mid+1, r)
 * At last, we perform the merging the halves of the array. We copy the left half of the elements
 * in one array and right half in another array. Then iterate till either of arrays sizes are reached,
 * and in each iteration check if ith index of left is greater than jth index of right. Which ever is 
 * smaller will be put in the lth index of the original array and update the respective index positions
 * on the respective halves. If any half has left over elements, push them to the array end indices.
 */
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int size1 = m - l + 1;
        int size2 = r - m;
 
        int left[] = new int[size1];
        int right[] = new int[size2];
 
        for (int i = 0; i < left.length; i++)
            left[i] = arr[l + i];
        for (int j = 0; j < right.length; j++)
            right[j] = arr[m + 1 + j];
 
        int i = 0, j = 0;
        int index = l;
        while (i < size1 && j < size2) {
            if (left[i] <= right[j]) {
                arr[index++] = left[i++];
            }
            else {
                arr[index++] = right[j++];
            }
        }

        while (i < size1) {
            arr[index++] = left[i++];
        }
 
        while (j < size2) {
            arr[index++] = right[j++];
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	if(l >= r)
    		return;
    	int mid = (l + r) / 2;
    	sort(arr, l, mid);
    	sort(arr, mid+1, r);
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