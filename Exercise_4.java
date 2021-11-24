//Timecomplexity : O(nlogn)
//space complexity : O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] left = new int[m-l+1];
       int[] right = new int[r-m];
      for(int i=0 ;i<left.length;i++){
          left[i]=arr[l+i];
      }
      for(int i=0;i<right.length;i++){
          right[i]=arr[m+i+1];
      }
      int a =0;
      int b=0;
      int c=l;
      while(a<left.length && b<right.length){
          if(left[a]<right[b]){
              arr[c]=left[a];
              c++;
              a++;
          }else{
              arr[c]=right[b];
              b++;
              c++;
          }
      }
      
      while(a<left.length){
          arr[c]=left[a];
          a++;
          c++;
      }
      
      while(b<right.length){
          arr[c]=right[b];
          b++;
          c++;
      } 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r){
            return;
        }
        int mid = l+(r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);     
        merge(arr,l,mid,r);      
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