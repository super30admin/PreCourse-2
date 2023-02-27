// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        // 2 temp arrays
        int[] left = new int[m-l+1];
        int[] right = new int[r-m];
        
        // set elements in temp arrays;
        for(int i = 0 ;i <m-l+1  ; i++){
            left[i] =arr[l+i];
        }

        for(int i = 0 ;i <r-m  ; i++){
            right[i] =arr[m+i+1];
        }

        // sort
        int x = 0, y= 0;
        int z = l;
        while(x<left.length && y< right.length){
            if(left[x] <= right[y]){
                arr[z++] = left[x++];
            }
            else if(right[y]<left[x]){
                arr[z++] = right[y++];
            }
        }

        // if size of left & right arrays are uneven copy remaining elements
        while(x<left.length){
            arr[z++] = left[x++];
        }
        while(y<right.length){
            arr[z++] = right[y++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    if(l<r){
        int mid =l + (r-l)/2;

        sort(arr, l, mid);
        sort(arr, mid+1, r);
        merge(arr, l, mid, r);
    }

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