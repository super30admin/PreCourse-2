package precourse2;
//time complexity:  O(nlogn)
//space complexity: n
class MergeSort 
{ 
	//Merges two sub arrays of arr[]. 
	//First sub array is arr[start..mid] 
	//Second sub array is arr[mid+1..end] 
    void merge(int arr[], int start, int mid, int end) 
    {  
    	// Find sizes of two sub arrays to be merged
        int arr1 = mid - start + 1;
        int arr2 = end - mid;
  
        // Create temp arrays
        int temp1[] = new int[arr1];
        int temp2[] = new int[arr2];
        for (int i = 0; i < arr1; ++i)
        	temp1[i] = arr[start + i];
        for (int j = 0; j < arr2; ++j)
        	temp2[j] = arr[mid + 1 + j];
        
        // Merge the temp arrays

        int i = 0, j = 0;
  
        // Initial index of merged sub array
        int k = start;
        while (i < arr1 && j < arr2) {
            if (temp1[i] <= temp2[j]) {
                arr[k] = temp1[i];
                i++;
            }
            else {
                arr[k] = temp2[j];
                j++;
            }
            k++;
        }
        // Copy remaining elements of temp1[] if any 
        while (i < arr1) {
            arr[k] = temp1[i];
            i++;
            k++;
        }
  
        // Copy remaining elements of temp2[] if any
        while (j < arr2) {
            arr[k] = temp2[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[start..end] using 
    // merge() 
    void sort(int arr[], int start, int end) 
    { 
    	 if (start < end) {
             int mid =start+ (end-start)/2;
             sort(arr, start, mid);
             sort(arr, mid + 1, end);
             merge(arr, start, mid, end);
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