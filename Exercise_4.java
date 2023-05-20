/*Time complexity
O(nlogn)
*/

/*Space complexity
O(n) as we are keeping a temp array for the merge step
*/

// Did this code successfully run on Leetcode : Yes but time limit was exceeded
// Any problem you faced while coding this : Had to take some time to learn to implement the merge function
class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int i = l;
        int j = m + 1;
        int k = i;
        int tempArr[] = arr.clone();
        while (i <= m && j <= r) {
            if (arr[i] <= arr[j]) {
                tempArr[k] = arr[i];
                i++;
                k++;
            } else {
                tempArr[k] = arr[j];
                j++;
                k++;
            }
        }

        while (i <= m) {
            tempArr[k] = arr[i];
            i++;
            k++;

        }

        while (j <= r) {
            tempArr[k] = arr[j];
            j++;
            k++;

        }

        for (int x = l; x <= r; x++) {
            arr[x] = tempArr[x];
        }

    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l==r){
            return;
        }
        int mid=(l+r)/2;

        sort(arr,l,mid);
        sort(arr,mid+1, r);
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