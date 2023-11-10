class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int leftArrSize=m-l+1;
        int rightArraySize=r-m;
        int leftArray[]= new int[leftArrSize];
        int rightArray[]= new int[rightArraySize];

        for (int i =0;i<leftArrSize;++i){
            leftArray[i]=arr[l+i];
        }
        for (int j =0;j<rightArraySize;++j){
            rightArray[j]=arr[m+1+j];
        }
        int i=0;
        int j=0;
        int k=l;
        //compare left and right array element and insert smallest in arr
        while (i<leftArrSize && j < rightArraySize){
            if (leftArray[i]<=rightArray[j]){
                arr[k]=leftArray[i];
                i++;
            }
            else {
                arr[k]=rightArray[j];
                j++;
            }
            k++;
        }
        //insert remaining elements if left array in arr
        while (i < leftArrSize) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        // insert remaining elements of right array in arr
        while (j < rightArraySize) {
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
    if (r>l){
        int mid=l+(r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);

    }
        //Call mergeSort from here 
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