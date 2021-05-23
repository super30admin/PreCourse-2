class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int left_array_length = m-l+1;
       int right_array_length = r-m;

       int left_arr[]=new int [left_array_length];
       int right_arr[]= new int [right_array_length];

       for(int i=0; i<left_array_length;++i){
           left_arr[i]=arr[l+i];
       }
       for(int j=0; j<right_array_length;++j){
         right_arr[j]=arr[m+1+j];
    }   
        int i = 0, j = 0;
        int k = l;
        while (i < left_array_length && j < right_array_length) {
            if (left_arr[i] <= right_arr[j]) {
                arr[k] = left_arr[i];
                i++;
            }
            else {
                arr[k] = right_arr[j];
                j++;
            }
            k++;
        }
                
        while (i < left_array_length) {
            arr[k] = left_arr[i];
            i++;
            k++;
        }
 
        while (j < right_array_length) {
            arr[k] = right_arr[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l < r){
            int mid=l+(r-l)/2;
            //Divide and sort the two derived list
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr, l, mid, r);
        }

	//Write your code here
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