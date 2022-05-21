class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        //Time Complexity=O(n^2)
        //Space Complexity=o(1)
       //Your code here
        //for the sake of traversing in the second part of array, store the start of second array
        int l2=m+1;
        //Check if the last element of the first array is smaller than the last element of the second array
        if(arr[m]<=arr[l2]){
            return;
        }
       while(l<=m && l2<=r){
           if(arr[l]<=arr[l2]){
               l++;
           }else{
               //shift the smaller element to the first array sfit the other elements to right
               int temp=arr[l2];
               int tempIndex=l2;
               while(tempIndex!=l){
                   arr[tempIndex]=arr[tempIndex-1];
                   tempIndex--;
               }
               arr[l]=temp;
               l++;l2++;m++;
           }
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        //Time Complexity=2T(n/2)+n^2->O(n)=(n^2 Logn)
        //Space Complexity=o(1)
	//Write your code here
        if(l<r){
            int m=l+(r-l)/2;
            sort(arr,l,m);
            sort(arr,m+1, r);
            //Call mergeSort from here
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