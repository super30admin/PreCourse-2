// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


// Your code here along with comments explaining your approach
/*
 * Divided list in two halves
 * and sorted the two halfs and merged them
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int left, int mid, int right) 
    {  
        int nL = mid - left + 1;
        int nR = right -mid;

        //creates temp left and right arrays
        int [] tempL = new int [nL];
        int [] tempR = new int [nR];

        //copies data from sub arrays in to this array
        for(int i = 0; i < nL; i++) {
            tempL[i] = arr[left + i];
        }
        for(int j = 0; j < nR; j++) {
            tempR[j] = arr[mid + 1 + j];
        }

        //Merge the temp arrays
        
        //Initial indices of the left and right subarrays
        int i =0, j = 0;

        //initial index of merged subarray
        int k = left;

        while (i < nL && j < nR) {
            if (tempL[i] <= tempR[j]) {
                arr[k] = tempL[i];
                i++;
            } else {
                arr[k] = tempR[j];
                j++;
            }
            k++;
        }

        //push remaining left subarray in merged array
        while (i < nL) {
            arr[k] = tempL[i];
            i++;
            k++;
        }

        while (j < nR) {
            arr[k] = tempR[j];
            j++;
            k++;
        }  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int left, int right) 
    { 
        if (left < right) {
            //Find mid point
            int mid = left + (right - left) / 2;

            //merge left array
            sort(arr, left, mid);

            //merge right array
            sort(arr, mid + 1, right);

            //combine the merge
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