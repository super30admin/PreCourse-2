//Overall Time Complexity is O(nlogn)
//Overall Space Complexity is O(n)


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int n1 = m - l  + 1; // left array size 
       int n2 = r - m; // right array size 

       int leftArray[] = new int[n1];
       int rightArray[] = new int[n2];

       for(int i = 0; i<n1; i++){ //Copy the data into leftvsubarray and right subarray 
        leftArray[i] = arr[l+i];
       }
       for(int j = 0; j<n2; j++){
        rightArray[j] = arr[m+1+j];
       }
       int i = 0, j = 0, k = l;
       while(i<n1 && j<n2){
        if(leftArray[i]<=rightArray[j]){ //Compare and merge the values into the main array 
            arr[k] = leftArray[i];
            i++;
        }
        else{
            arr[k] = rightArray[j];
            j++;
        }
        k++;
       }

       while(i<n1){ 
        arr[k] = leftArray[i];
        i++;
        k++;
       }
       while(j<n2){
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
        //Call mergeSort from here 
        if(l<r){
            int mid = l + (r-l)/2;

            sort(arr,l,mid);       // Split into 2 arrays
            sort(arr, mid + 1, r);  

            merge(arr,l, mid, r);

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