class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int n1 = m - l +1; //size of left part
       int n2 = r - m;  //size of right part
       
       int left[] = new int[n1];
       int right[] = new int [n2];

       //copy left half int left[]
       for(int i = 0; i<n1; i++)
        left[i] = arr[ l + i ];
       //copy right hlaf into right[]
       for(int j = 0;j< n2;j++)
        right[j] = arr[m+1+j];

       int i =0; //pointer for left[]
       int j =0; //pointer for right[]
       int k =l; //pointer for original arr[]

       //compare both arrays and put smaller elemnt first
       while(i<n1 && j< n2){
        //left =[11,12,13]
        //right = [5,6,7]
        //comapre 11 and 5
        //5 is smaller so put 5 first
        if(left[i] <= right[j]){
            arr[k] = left[i];
            i++;
        }else{
            arr[k] = right[j];
            j++;
        }
        k++;
       }
       //if anything is still left in left[], copy it
       while(i<n1){
        arr[k] = left[i];
        i++;
        k++;
       }
       //if anything is still left in riight [], copy it 
       while(j<n2){
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
            int m = l+(r-l)/2;
            //srt left half
            sort(arr, l, m);
            //srt right half
            sort(arr,m+1, r);
            //merge both sorted halves
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