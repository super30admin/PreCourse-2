//Time complexity: O(n*logn)
//Space complexity: O(n)

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int nl = m - l + 1;
        int nr = r - m ;

        int left[] = new int[nl];
        int right[] = new int[nr];

        for (int i = 0 ; i < nl; i++){
            left[i] = arr[i + l];
        }
        for (int j = 0; j < nr; j ++){
            right[j] = arr[j + m + 1];
        }


        int i = 0 , j = 0;
        int k = l;

        while (i < nl && j < nr){
            if (left[i] <= right[j]){
                arr[k] = left[i];
                i++;
            }
            else{
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < nl){
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < nr){
            arr[k] = right[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if (l < r) {
            int middle = l + (r - l) / 2;

            sort(arr, l , middle);

            sort(arr, middle + 1, r);

            merge(arr, l , middle , r);
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