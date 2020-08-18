class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  

       int sizeL = m - l + 1;
       int sizeR = r - m;

       int[] L = new int[sizeL];
       int [] R = new int[sizeR];

       for(int i = 0; i < sizeL ; i++) {
            L[i] = arr[l+i];
       }
        
        for(int i = 0; i < sizeR ; i++) {
            R[i] = arr[i + (m+1)];
       }

       int i = 0, j = 0, k = l;

       while(i < sizeL && j < sizeR) {
           if(L[i] < R[j]) {
               arr[k] = L[i];
               i++;
           } else {
            arr[k] = R[j];
            j++;
           }
           k++;
       }

       while(i < sizeL) {
        arr[k] = L[i];
        i++;
        k++;
       }

       while(j < sizeR) {
        arr[k] = R[j];
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
        if(l >= r) {
            return;
        }
        
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