// Time complexity: o(n * log n)
// Space complexity: O(n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       // Create left & right sub arrays
       int left_size = m - l +1;
       int right_size = r - m;
       int[] left_array = new int[left_size];
       int[] right_array = new int[right_size];

        // Put the data in these sub arrays
        System.arraycopy(arr, l, left_array, 0, left_size);
        for(int j = 0 ; j < right_size;j ++){
            right_array[j] = arr[m + 1 + j];
        }

        int left_array_index, right_array_index, main_array_index;
        left_array_index = 0;
        right_array_index = 0;
        main_array_index = l;

        // Compare left sub array with right sub array
        while(left_array_index < left_size && right_array_index < right_size){
            if(left_array[left_array_index] < right_array[right_array_index]){
                arr[main_array_index] = left_array[left_array_index];
                left_array_index++;
            }else{
                arr[main_array_index] = right_array[right_array_index];
                right_array_index++;
            }
            main_array_index++;
        }

        // copy left over elements
        while(left_array_index < left_size){
            arr[main_array_index] = left_array[left_array_index];
            main_array_index++;
            left_array_index++;
        }
        while(right_array_index < right_size){
            arr[main_array_index] = right_array[right_array_index];
            main_array_index++;
            right_array_index++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    if (l < r){
            int mid = (l + r) / 2;

            // Divide
            sort(arr,l,mid);
            sort(arr, mid+1, r);

            // and conquer
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
        int arr[] = {12, 11, 13, 5, 6, 7, 1};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 