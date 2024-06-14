//Time Complexity: O(nlogn)
//Space Complexity: O(n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int leftArraySize = m - l +1;
       int rightArraySize = r -m;

       // create temporary arrays
        int leftArray[] = new int[leftArraySize];
        int rightArray[] = new int[rightArraySize];

        // copying data to temporary arrays
        for(int i=0; i<leftArraySize; i++){
            leftArray[i] = arr[l + i];
        }
        for(int j=0; j<rightArraySize; j++){
            rightArray[j] = arr[m +1 + j];
        }

        int i=0, j=0, k=l;

        while(i <leftArraySize && j <rightArraySize) {
            if(leftArray[i] < rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // copying rest of the elements
        while(i < leftArraySize) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        while(j < rightArraySize) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l < r) {
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            //Call mergeSort from here
            merge(arr, l, mid,r);
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