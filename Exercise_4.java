//Time Complexity = O(n logn), Space complexity = n

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int []arr, int beg, int mid, int end)
    {
          int i = beg, j = mid + 1, index = beg;
          int []temp = new int[10];
          int k;
          while((i<=mid) && (j<=end))
          {
              if(arr[i]<arr[j]){
                  temp[index] = arr[i];
                  i++;
              }
              else{
                  temp[index] = arr[j];
                  j++;
              }
              index++;
          }
          if(i>mid){
              while(j<=end){
                  temp[index]=arr[j];
                  j++;
                  index++;
              }
          }
          else{
              while(i<=mid){
                  temp[index] = arr[i];
                  i++;
                  index++;
              }
          }
          for(k=beg;k<index;k++){
              arr[k]=temp[k];
          }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
   void sort(int []arr, int beg, int end)
    {
        int mid;
        if(beg<end){
            mid = (beg+end)/2;
            sort(arr,beg,mid);
            sort(arr,mid+1,end);
            merge(arr,beg,mid,end);
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
