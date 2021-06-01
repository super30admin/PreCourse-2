// Time Complexity : O(n log n)
// Space Complexity : O(n)

public class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
// take length of both arrays as s1 and s2
        int s1 = m - l + 1;
        int s2 = r - m;
        /* Create left and right side arrays */
        int LeftSide[] = new int[s1];
        int RightSide[] = new int[s2];

        /*add elements to left and right arrays created*/
        for (int a = 0; a < s1; ++a)
            LeftSide[a] = arr[l + a];
        for (int b = 0; b < s2; ++b)
            RightSide[b] = arr[m + 1 + b];

        int i = 0, j = 0;
        int k = l;
        while (i < s1 && j < s2) {
            if (LeftSide[i] <= RightSide[j]) {
                arr[k] = LeftSide[i];
                i++;
            }
            else {
                arr[k] = RightSide[j];
                j++;
            }
            k++;
        }

        /* Take remaining LeftSide[] elements*/
        while (i < s1) {
            arr[k] = LeftSide[i];
            i++;
            k++;
        }

        /* Take remaining RightSide[] elements */
        while (j < s2) {
            arr[k] = RightSide[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if (l < r) {
            // r-l to prevent integer overflow
            int m =l+ (r-l)/2;
            // run sort on both sides
            sort(arr, l, m);
            sort(arr, m + 1, r);
            // Merge the sorted sides
            merge(arr, l, m, r);
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