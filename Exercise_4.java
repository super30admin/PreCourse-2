class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int[] left = new int[mid - l + 1];
        int[] right = new int[r - mid];
       int j = l, k = mid+1;
        for (int i = 0; i < mid - l+1; i++) //left[i] = arr[l+i];
            left[i] = arr[j++];
        for (int i = 0; i < r-mid; i++) //right[i] = arr[mid+i+1];
            right[i] = arr[k++];

        System.out.println(Arrays.toString(left));
        System.out.println(Arrays.toString(right));
        k=1;
        j=0;
        int i=0;
        while((i<mid-l+1)&&(j<r-mid)){
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

    }

  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    //Write your code here
    int mid=(l+r)/2;
        //Call mergeSort from here 
        sort(arr,l,mid-1);
        sort(arr,mid,r);
        merge(arr,l,mid,r);
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