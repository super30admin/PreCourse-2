//Time Complexity : O(N logN)
//Space Complexity : O(N)
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

        int[] leftArr = new int[leftSize];
        int[] rightArr = new int[rightSize];

        //Copy the range of left to mid from original array to leftArr
        for(int i=0; i<leftSize; i++)
            leftArr[i] = arr[l+i];

        //Copy the range of mid+1 to right from original array to rightArr
        for(int i=0; i<rightSize; i++)
            rightArr[i] = arr[m+1+i];

        //Compare the elements of leftArr and rightArr and place the smaller one in original arr
        int i=0, j=0, index=l;
        while (i<leftSize && j<rightSize) {

            if(leftArr[i] <= rightArr[j]) {
                arr[index] = leftArr[i];
                i++;
            }
            else {
                arr[index] = rightArr[j];
                j++;
            }
            index++;
        }

        //If all elements of leftArr are not copied into original arr, then do so
        while (i < leftSize) {
            arr[index] = leftArr[i];
            i++;
            index++;
        }

        //If all elements of rightArr are not copied into original arr, then do so
        while(j < rightSize) {
            arr[index] = rightArr[j];
            j++;
            index++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        //break the array into 2 till the length of the array is 1, then call merge
        if(l < r) {
            int m = l+(r-l)/2;

            sort(arr, l, m);
            sort(arr, m+1, r);

            merge(arr, l, m, r);
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