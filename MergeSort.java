// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int llength = m-l+1;
       int rlength = r-m;
       
       int larr[]=new int[llength];
       int rarr[]=new int[rlength];

       //Copy all the elements from the low to middle index of the main array in to the  left array & all the elements from the middle to high index of the main array in to the right array 
       for(int i=0;i<llength;i++){
        larr[i]=arr[l+i];
       }

       for(int j=0;j<rlength;j++){
        rarr[j]=arr[m+1+j];
       }

       ///Starting from the 0th index of both the arrays compare each element one by one such that the smaller element is written into the array first. 
       //variables to keep track of the left array, right array and main array indices respectively
       int i=0,j=0,index=l;
       //Iterate until atleast one of the arrays is fully traversed
       while(i<llength && j<rlength){
        //if the left array element is smaller then its written into the main array
        if(larr[i]<=rarr[j]){
            arr[index]=larr[i];
            i++;
        }else{
            //else if the right array element is smaller then its written into the main array
            arr[index]=rarr[j];
            j++;
        }
        index++;
       }

       //check if left array is not completely traversed, if yes, then copy the remaining elements into the main array 
       while(i<llength){
        arr[index]=larr[i];
        i++;
        index++;
       }

       //check if right array is not completely traversed, if yes, then copy the remaining elements into the main array 
       while(j<rlength){
        arr[index]=rarr[j];
        j++;
        index++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //recursion stopping condition - until there are atleast 2 elements in every subarray
        if(l<r){
            //find middle index
            int m = (l+r)/2;
            //sort the elements from the low index to the middle element
            sort(arr, l, m);
            //sort the elements from the midle +1 index to the high index
            sort(arr, m+1, r);

            //merge when further division is not possible
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