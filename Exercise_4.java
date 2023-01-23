class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int start, int mid, int end) 
    {  
       //Your code here  
       int[] mix = new int[end - start];
       int i = start;
       int j = mid;
       int k = 0;

       while(i < mid && j < end){
        if(arr[i] < arr[j]){
            mix[k] = arr[i];
            i++;
        } else {
            mix[k] = arr[j];
            j++;
        }
        k++;
        }
        //it may be possible that one of the arrays isn't complete
        //copy the remaining elements
        while(i < mid){
            mix[k] = arr[i];
            i++;
            k++;     
          }
       while(j < end){
        mix[k] = arr[j];
            j++;
            k++; 
       }  
       for(int l = 0; l < mix.length; l++){
        arr[start + l] = mix[l];
       }
       } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int start, int end) 
    { 
	//Write your code here
    if(end - start == 1){
        return;
    }

    int mid = start + (end - start)/2;

        //Call mergeSort from here 
        sort(arr, start, mid);
        sort(arr, mid, end);

        merge(arr, start, mid, end);
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
        ob.sort(arr, 0, arr.length); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 