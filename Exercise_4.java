class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftArrayEnd = m-l +1;
        int rightArrayStart = r - m;

        int[] leftTempArray = new int[leftArrayEnd];
        int[] rightTempArray = new int[rightArrayStart];

        for (int i = 0; i < leftArrayEnd; ++i)
            leftTempArray[i] = arr[l + i];
        for (int j = 0; j < rightArrayStart; ++j)
            rightTempArray[j] = arr[m + 1 + j];

        int i = 0, j = 0;
        int k = l;
        while (i < leftArrayEnd && j < rightArrayStart) {
            if (leftTempArray[i] <= rightTempArray[j]) {
                arr[k] = leftTempArray[i];
                i++;
            }
            else {
                arr[k] = rightTempArray[j];
                j++;
            }
            k++;
        }

        while (i < leftArrayEnd) {
            arr[k] = leftTempArray[i];
            i++;
            k++;
        }

        while (j < rightArrayStart) {
            arr[k] = rightTempArray[j];
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
        if(l>=r){
            return;
        }
        int middle = l+(r-l)/2;
        sort(arr, l, middle);
        sort(arr, middle+1, r);

        merge(arr, l, middle, r);
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