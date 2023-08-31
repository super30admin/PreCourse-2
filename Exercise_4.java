//Time Complexity O(n log n) space complexity O(n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftSize = m-l+1;
        int rightSize = r-m;

        int[] leftArray = new int[leftSize];
        int[] rightArray = new int[rightSize];

        for (int i = 0; i < leftSize; ++i)
            leftArray[i] = arr[l + i];
        for (int j = 0; j < rightSize; ++j)
            rightArray[j] = arr[m + 1 + j];


        int i=0,j=0,k=l;

        while(i<leftSize && j<rightSize){
            if(leftArray[i]<=rightArray[j])
                arr[k++] = leftArray[i++];
            else
                arr[k++] = rightArray[j++];

        }
        while (i<leftSize)
            arr[k++] = leftArray[i++];

        while (j<rightSize)
         arr[k++] = rightArray[j++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l<r){
           int m = l+(r-l)/2;
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