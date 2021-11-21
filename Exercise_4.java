class MergeSort 
{  
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       // First subarray is arr[l..m]
        int len1=  m-l+1;
        int left[]=new int[len1];
        for (int i = 0; i < len1; ++i)
            left[i] = arr[l + i];
        // Second subarray is arr[m+1..r]
        int len2 = r-m;
        int right[]=new int[len2];
        for (int j = 0; j < len2; ++j)
            right[j] = arr[m + 1 + j];

        // Merges two subarrays of arr[]. 
        int i=0;
        int j=0;
        int k=l;
        while(i<len1 && j<len2){
            //compare respective array elements;
            if(left[i]<=right[j]){
                arr[k]=left[i];
                i++;
            }
            else{
                arr[k]=right[j];
                j++;
            }
            k++;
        }
        //deal with the end of remaining elements from left and rifht arrays if any.
        while(i<len1){
            arr[k]= left[i];
            i++;
            k++;
        }
        while(j<len2){
            arr[k]=right[j];
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
        int  m;
        if(l<r){
            m= (l+r)/2;
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
        int arr[] = {12, 11, 13, 5, 6, 0, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 