class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int n = arr.length;
       int temp[] = new int[n];
       int size = r - l + 1;
       //int m = (l+r)/2;
       int leftEnd = (l + r) / 2;
       int rightStart = leftEnd + 1;
       int left = l;
       int right = rightStart;
       int index = left;
       while(left <= leftEnd && right <= r) {
           if(arr[left] <= arr[right]) {
               temp[index] = arr[left];
               left++;
           }
           else {
               temp[index] = arr[right];
               right++;
           }
           index++;
       }
       System.arraycopy(arr,left,temp,index,leftEnd-left+1);
       System.arraycopy(arr,right,temp,index,r-right+1);
       System.arraycopy(temp,l,arr,l,size);
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        int m = l + (r-l)/2;
        if(l<r) {
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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