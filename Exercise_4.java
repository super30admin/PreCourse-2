//Time Complexity : O (n log n)
// Space Complexity : O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
    int i, j, k;  
    int size1 = m - l + 1;    
    int size2 = r - m;    
    int LeftArray[] = new int[size1];
    int RightArray[]= new int[size2];  
    for ( i = 0; i < size1; i++)    
    LeftArray[i] = arr[l + i];    
    for (j = 0; j < size2; j++)    
    RightArray[j] = arr[m + 1 + j];    
    i = 0; 
    j = 0;   
    k = l;      
    while (i < size1 && j < size2) {    
        if(LeftArray[i] <= RightArray[j]) {    
            arr[k] = LeftArray[i];    
            i++;    
        }    
        else {    
            arr[k] = RightArray[j];    
            j++;    
        }    
        k++;    
    }    
    while (i<size1) {    
            arr[k] = LeftArray[i];    
            i++;    
            k++;    
        }    
      
    while (j<size2) {    
            arr[k] = RightArray[j];    
            j++;    
            k++;    
        }     
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l < r) {
            int mid = (l + r) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
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