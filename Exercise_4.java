// Time Complexity : n log(n)
// Space Complexity : n 
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :
// Code not running completely. Will push correct code later on, as I am currently facing some issues with it. 

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    //    //Your code here  

    //    //Find sizes of the two arrays
        int s1 = m - l + 1;
        int s2 = r - m;
  
        //Temp arrays
        int temp_left[] = new int[s1];
        int temp_right[] = new int[s2];
  
        //Copy data into temporary arrays
        for (int i = 0; i < s1; ++i)
            temp_left[i] = arr[l + i];
        for (int j = 0; j < s2; ++j)
            temp_right[j] = arr[m + 1 + j];
  
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
  
        // Initial index of merged subarray array
        int k = l;
        
        //Merging temporary arrays
        while (i < s1 && j < s2) {
            if (temp_left[i] <= temp_right[j]) {
                arr[k] = temp_left[i];
                i++;
            }
            else {
                arr[k] = temp_right[j];
                j++;
            }
            k++;
        }
  
        //Copy the remaining elements of left array if any exist 
        while (i < s1) {
            arr[k] = temp_left[i];
            i++;
            k++;
        }
  
        //Copy the remaining elements of right array if any exist 
        while (j < s2) {
            arr[k] = temp_right[j];
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
        if(l<r) {
            //Middle point:
            int middle = l + (r-1)/2;

            //Sort both halves
            sort(arr, l, middle);
            sort(arr, middle + 1, r);

            merge(arr, l, middle, r);

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