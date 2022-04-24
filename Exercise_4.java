class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int subArray1=m-l+1;
        int subArray2=r-m;

        //Create a temp Array;
        int tempArray1[] = new int[subArray1];
        int tempArray2[] = new int[subArray2];

        for(int i=0;i<subArray1;i++){
            tempArray1[i]= arr[l+i];
        }

        for(int j=0;j<subArray2;j++){
            tempArray2[j]=arr[m+1+j];
        }

        int i=0;
        int j=0;
        int k=0;

        while(i<subArray1 && j<subArray2){

            if(tempArray1[i]<=tempArray2[j]){
                arr[k]=tempArray1[i];
                i++;
            }else{
                arr[k] = tempArray2[j];
                j++;
            }
            k++;
        }

        while (i<subArray1){
            arr[k]= tempArray1[i];
            i++;
            k++;
        }

        while (j<subArray2){
            arr[k]= tempArray2[j];
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

        while(l<r){
            int mid = (l+r)/2;

            sort(arr,l,mid);
            sort(arr,mid+1,r);

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