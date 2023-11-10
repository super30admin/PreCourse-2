/*
    Time complexity - O(nlogn)
    Space complexity - O(n)
*/
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int size_1 = m-l+1;
       int size_2 = r-m;
       int Arr1[] = new int[size_1];
       int Arr2[] = new int[size_2];

       for(int i=0; i<size_1; ++i)
            Arr1[i] = arr[l+i];
        for(int j=0; j<size_2; ++j)
            Arr2[j] = arr[m+1+j];

    int i=0;
    int j=0;
    int k=l;
    while( i<size_1 && j<size_2){
        if( Arr1[i] <= Arr2[j]){
            arr[k] = Arr1[i];
            i++;
        }
        else{
            arr[k] = Arr2[j];
            j++;
        }
        k++;
    }    

    while(i< size_1){
        arr[k] = Arr1[i];
        i++;
        k++;
    }
    while (j < size_2){
        arr[k] = Arr2[j];
        j++;
        k++;
    }
        

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    if(l<r){
        int m= l + (r-l)/2;
        System.out.println(m);
        sort(arr,l,m);
        sort(arr,m+1,r);
        //Call mergeSort from here
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