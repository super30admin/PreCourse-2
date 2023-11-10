//Time complexity = O(nlogn)
//Space complexity = O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //The sizes of two arrays to be merged
       int arr1 = m-l + 1;
       int arr2 = r-m;
       //Create temporary arrays
       int L[] = new int[arr1];
       int R[] = new int[arr2];
       //Copy the data into temp arrays
       for(int i=0;i<arr1;i++)
            L[i] = arr[l+i];
       for(int j=0;j<arr2;j++)
            R[j] = arr[m+1+j];
        //MErge 2 temp arrays
        //initial indexes for first and second array
        int i = 0, j=0;
        //inital index of merged subarray
        int k =l;
        while(i<arr1 && j<arr2)
        {
            if(L[i]<=R[j]){
                arr[k] = L[i];
                i++;
            }else{
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        //copy remaining elements of L[] if any 
        while(i<arr1){
            arr[k] = L[i];
            i++;
            k++;
        }
        //copy remaining elements of R[] if any from right
        while(j<arr2){
            arr[k] = R[j];
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
            int m = l + (r-l)/2;//find middle point
            //sort first and second halves
            sort(arr,l,m);
            sort(arr,m+1,r);
            //merge the sorted halves
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