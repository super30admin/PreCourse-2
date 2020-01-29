class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //creating the new array for the sorting purposes 
        int [] sortArray = new int [arr.length] ;

        //for filling up the new array 
        int index = 0 ;  
        //to use while filling original array towards the end 
        int low = l ; 

        //bounds for the low 
        int lowBound = m - 1 ;

        //the actual size of the array off the original array 
        int size = r - low + 1 ;  

        //looping through both the array and actually merging here 
        while (l <= lowBound && m <= r) {
            if (arr[l] < arr[m])
                sortArray[index++] = arr[l++]; 
            else
                sortArray[index++] = arr[m++] ; 
        }

        //when one of the array gets empty 
        while (l <= lowBound)
            sortArray[index++] = arr[l++] ; 
        while (m <= r )
            sortArray[index++] = arr[m++] ; 

        //now copying the sorted array back to the original array 
        for (int i = 0 ; i < size ; i++){
            arr[i + low] = sortArray[i] ; 
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	   //base case 
        if (l == r)
            return ; 
        //finding the middle 
        int mid = (r + l) / 2 ;

        //recursive calls 
        sort(arr, l, mid) ; 
        sort(arr, mid + 1 , r) ; 

        //calling the merge method the recursive calls the base case and clears the call stack to merge the individually sorted arrays of size 1  
        merge(arr, l, mid + 1, r) ; 
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