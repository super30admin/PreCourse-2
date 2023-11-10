//Time complexity is O(nlogn)
//space complexity is o(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int leftPart = m - l + 1;
       int rightPart = r - m;
   
       int tempL = new int[leftPart];
       int tempR = new int[rightPart];
       for (int i = 0; i < leftpart; i++)
         tempL[i] = arr[l+i];
       for(int j = 0; j < rightPart; j++)
          tempR[j] = arr[m+1+j];

       int i = 0, j = 0;
       int k = l;
       while(i < leftPart && n2 < rightPart){
         if (tempL[i] <= tempR[i]){
         arr[k] = tempL[i];
         i++;
      } else {
             arr[k] = tempR[j];
             j++;
   }
   k++; 
         
    } 
   
   while(i < leftPart){
     arr[k] = tempL[i];
     i++;
     k++;
    }
    
   while(j < rightPart){
   arr[k] = tempR[j];
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
       if (l < r){
     int mid = l+ (r-l)/2;
     sort(arr,l,m);
     sort(arr,m+1,r);
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
