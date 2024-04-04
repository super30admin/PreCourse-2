// Time Complexity : Best case O(n log n) and Worst case O(N^2)
// Space Complexity : O(N) where N is the size of the array
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int n = arr.length;
       // int mid = n/2;

        //creating 2 temp arrays left and right sub arrays
        int leftArray[] = new int[m];
        int rightArray[] = new int[n-m];

        // copying elements till mid to left subarray
        for(int i=0;i<m;++i){
            leftArray[i] = arr[i];
        }

        // copying elements to from mid to endin right sub array
        for(int i=m;i<n;i++){
            rightArray[i-m]= arr[i];
        }

        int leftSize = leftArray.length;
        int rightSize= rightArray.length;

        int i=0; int j=0;
        int k = 0;

        // merging sub arrays to original array
        while(i < leftSize && j < rightSize) {
            if(leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            }else{
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }
        // copy remaining elements from leftArray
        while(i < leftSize) {
            arr[k]= leftArray[i];
            i++;
            k++;
        }
        // copy remaining elements from rightArray
        while(j < rightSize) {
            arr[k]= rightArray[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        // Call mergeSort from here
       if(l < r){
           int mid = l + (r-l)/2;
           sort(arr, l, mid);
           sort(arr, mid+1, r);
           merge(arr,l,mid,r);
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