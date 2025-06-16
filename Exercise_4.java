// Time Complexity: O(n log n)
// Space Complexity: O(n) due to the temporary array used in merge()
// Any problem you faced while coding this : no

/* Approach :-
 * Sort function:
 * 1. In this function we will divide the array in 2 subarrays till we are left with a single element 
 * 2. We will call the merge function after we are done splitting the array into smaller subarrays
 * 
 * Merge function:
 * In this function we will merge the 2 subarrays that we got from the sort function
 * 
 * 1. We will create a new temp array of the size (r-l+1), and initialize 2 variables left from l and right  from m+1
 * 
 * 2. We will run a while loop till left<=m and right <= r and compare the elements arr[left] and arr[right],
 *    whichever element is smaller will get stored in the temp array
 * 
 * 3. There is a possibility that either left side of the array or right 
 *    side of the array wasn't iterated till end so we can run while loop
 *    for both the cases and store the element in the temp array
 * 
 * 4. Now we want to store the sorted order in the orignal array and 
 *   hence we will run a for loop and store the elements in the original array
 */

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int temp[] = new int[r-l+1];
       int left = l;
       int right = m+1;
       int i = 0;

       while(left <= m && right <= r){
            if(arr[left] <= arr[right]){
                temp[i] = arr[left];
                left++;
            }
            else{
                temp[i] = arr[right];
                right++;
            }
            i++;
       }

       while(left <= m){
        temp[i] = arr[left];
        i++;
        left++;
       }

       while(right<=r){
        temp[i] = arr[right];
        i++;
        right++;
       }

       for(int j=0; j<temp.length; j++){
        arr[l+j] = temp[j];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l >= r) return;

        int mid = l + (r-l)/2;

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