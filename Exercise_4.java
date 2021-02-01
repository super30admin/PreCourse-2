//TC - O(nlogn), SC - O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int x = m-l+1;
        int y = r-m;
        int left[] = new int[x];
        int right[] = new int[y];

        for (int i = 0; i < x; i++)
            left[i] = arr[l+i];
        for (int j = 0; j < y; j++)
            right[j] = arr[m+1+j];

       //Your code here  
       int i = 0, j=0, k = l;

       while(i<x && j<y){
          if(left[i]<right[j])
            arr[k++] = left[i++];
          else    
            arr[k++] = right[j++];
       }

        while(i<x)
          arr[k++] = left[i++];
        
        while(j<y)
          arr[k++] = right[j++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if(l>=r)
            return;
        //Call mergeSort from here
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
        int arr[] = {10, 7, 8, 9, 1, 5}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 