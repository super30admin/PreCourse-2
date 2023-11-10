import java.util.Arrays;

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int len1 = m - l + 1;
        int len2 = r - m;

        /* Create temp arrays */
        int LEFT[] = new int[len1];
        int RIGHT[] = new int[len2];


        LEFT = Arrays.copyOfRange(arr, l , l + len1);
        RIGHT = Arrays.copyOfRange(arr, m+1, m+1 + len2);


        int i = 0, j = 0;


        int k = l;
        while (i < len1 && j < len2) {
            if (LEFT[i] <= RIGHT[j]) {
                arr[k] = LEFT[i];
                i++;
            }
            else {
                arr[k] = RIGHT[j];
                j++;
            }
            k++;
        }

        while (i < len1) {
            arr[k] = LEFT[i];
            i++;
            k++;
        }

        while (j < len2) {
            arr[k] = RIGHT[j];
            j++;
            k++;
        }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {

        if (l < r) {
            // Find the middle point
            int mid =l+ (r-l)/2;

            // Sort first and second halves
            sort(arr, l, mid);
            sort(arr, mid + 1, r);

            // Merge the sorted halves
            merge(arr, l, mid, r);
        }


	    //Write your code here
        //Call mergeSort from here 
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


/*

Time complexity : O (nlogn)

Space complexity : O (n) extra array


 */
