class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        //find sizes of two sub arrays to be merged.
        int n1= m-l+1;
        int n2 = r-m;

        //create two arrays left and right
        int left[] = new int[n1];
        int right[] = new int[n2];


        //copy the data into the temp arrays
        for(int i=0;i<n1;i++){
            left[i] = arr[l+i];
        }
        for(int j=0;j<n2;j++){
            right[j] = arr[m+1+j];
        }

        //merge the temp arrays
        int i=0,j=0;
        int k=l;
        while(i<n1 && j<n2){
            if(left[i]<=right[j]){
                arr[k] = left[i];
                i++;
            }else{
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        //copy remaining items of left array if any
        while(i<n1){
            arr[k]= left[i];
            i++;
            k++;
        }

        //copy the remaining items of right array if any
        while(i<n2){
            arr[k] = right[j];
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
            int middle = (l+r)/2;
            sort(arr, l, middle);
            sort(arr, middle+1, r);
            //merge the sorted halves
            merge(arr, l, middle, r);
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