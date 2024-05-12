class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int index1 = l;
        int index2 = m + 1;
        int i =0;

        int mergedArray[] = new int[r - l + 1];

        while(index1 <= m && index2 <= r){
            if(arr[index1] <= arr[index2])
            {
                mergedArray[i] = arr[index1];
                i++;
                index1++;
            }
            else{
                mergedArray[i] = arr[index2];
                i++;
                index2++;
            }
        }

        while(index1 <= m){
            mergedArray[i] = arr[index1];
            i++;
            index1++;
        }

        while(index2 <= r){
            mergedArray[i] = arr[index2];
            i++;
            index2++;
        }

        for(int k =0, j =l; k<mergedArray.length ; k++, j++){
arr[j] = mergedArray[k];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l >= r)
            return;

        int mid = l + (r-l)/2;
        sort(arr, l, mid);
        sort(arr, mid + 1, r);
        merge(arr, l , mid , r);
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