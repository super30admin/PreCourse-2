class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] leftArray = new int[m-l+1];
       int[] rightArray = new int[r-m];
       for (int i=0; i<leftArray.length; i++){
           leftArray[i] = arr[i+l];
       }
       for(int j=0; j<rightArray.length; j++){
           rightArray[j] = arr[j+m+1];
       }

       int x=0, y=0;
       int k=l;
       while(x<leftArray.length && y<rightArray.length){
           if(leftArray[x] <= rightArray[y]){
               arr[k] = leftArray[x];
               x++;
           }else{
               arr[k] = rightArray[y];
               y++;
           }
           k++;
       }
       while(x<leftArray.length){
           arr[k] = leftArray[x];
           x++;
           k++;
       }
       while(y<rightArray.length){
           arr[k] = rightArray[y];
           k++;
           y++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
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