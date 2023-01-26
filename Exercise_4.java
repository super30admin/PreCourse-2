//TC: O(nlogn)
//SC: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //find size of two subarrays to be merged
       int n1 = l + m -1;
       int n2 = r - m;

       //create temp arrays
       int left[] = new int[n1];
       int right[] = new int[n2];

       //copy data into temp arrays
       for(int i = 0; i<n1; i++){
        left[i] = arr[l+i-1];
       }

       for(int j = 0; j<n2; j++){
        right[j] = arr[m+j];
       }
       
        // Initial indexes of first and second subarrays
        int i=0, j=0;

        // Initial index of merged subarray array
        int k = l;

        while(i<n1 && j<n2){
            if(left[i] < right[j]){
                arr[k] = left[i];
                i++;
            }else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        //copy remaining elements of left[] if any
        while(i < n1){
            arr[k] = left[i];
            i++;
            k++;
        }

        //copy remaining elements of right[] if any
        while(j < n2){
            arr[k] = right[j];
            j++;
            k++;
        }




    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here //Call mergeSort from here 

        if(l<r){
            int mid = l + (r-l)/2;
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
