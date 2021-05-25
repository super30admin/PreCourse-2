public class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        
        //Time complexity of Mergesort is O(nlogn) since it divides the array into two halves
        //Space complexity is O(n) taking auxiliary space
       //Your code here  
    
        int len1 = m - l + 1;
        int len2 = r - m;
 
        /* Create two temporary arrays */
        int Left[] = new int[len1];
        int Right[] = new int[len2];
 
        /*Copy  the data to temporary arrays*/
        for (int i = 0; i < len1; ++i)
            Left[i] = arr[l + i];
        for (int j = 0; j < len2; ++j)
            Right[j] = arr[m + 1 + j];
 
        /* Merge the temp arrays */
 
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
 
        // Initial index of merged subarray array
        int k = l;
        while (i < len1 && j < len2) {
            if (Left[i] <= Right[j]) {
                arr[k] = Left[i];
                i++;
            }
            else {
                arr[k] = Right[j];
                j++;
            }
            k++;
        }
 
        /* Copy remaining elements of Left[] if any */
        while (i < len1) {
            arr[k] = Left[i];
            i++;
            k++;
        }
 
        /* Copy remaining elements of Right[] if any */
        while (j < len2) {
            arr[k] = Right[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Calling mergeSort from here 
        if(l < r)
        {
            //finding the middle element
            int mid = l + (r-l)/2;
            
            //sorting the first and second halves
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            
            //merge the subarrays using merge function
            merge(arr,l,mid,r);
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