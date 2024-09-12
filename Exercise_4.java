//Time Complexity : N(log N) --> best/worst case scenario
//Space Complexity : O(N)  -> everytime new temp list is created for n elements
// Merge Sort is better than quick sort in terms of time complexity for the worst case scenaio. However if space complexity matters then Quick sort is better because quick sort does sorting in "in place" whereas merge sort takes extra space as new temp array has to be created everytime for sorting the list


/**** Steps ****/
/*
1) Merge
     a) Create a temp array of size rightIndex(r) - leftIndex(l) + 1, so that elements can be sorted and stored in it
     b) Assume leftIndex(l) till mid(m) as one array and another array from mid(m)+1 till rightIndex(r) 
     c) Place the pointers on first element of both the list and start comparison for placing smaller element in the temp array. One pointer will be at l and another  pointer will be at m+1;
     d) Do check whether all the elements of the both the arrays are traversed and placed in the temp array
     e) After doing the above steps, place the temp array elements into the main array starting from leftIndex till rightIndex

2) Sort
      a) Find mid of the list using l and r
      b) Then call sort function from left(l) till mid(m)
      c) Then again call sort function from mid(m)+1 till right(r)
      d) Call the merge function for merging index elements ranging from left(l) to right(r). Here mid(m) is also passed so that we can split/partition our array into two list which is left and right. Left list which is from l to m and the right list which is from m+1 to r
      e) Call all the steps stated above recursively until l is less than r 
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       //Creating Temp array for sorting the elements while merging arrays 
       int tempArrSize = r-l+1;//will give total number of elements 
       int tempArr[] = new int[tempArrSize];
       int i=l; //pointing towards starting element of first list
       int j=m+1; //pointing towards starting element of second list which is going to start from mid+1
       int k=0;
       
       while(i<=m && j<=r){
           //Comparing first element of both the lists
           if(arr[i]<arr[j]){
               tempArr[k] = arr[i++];
           }else{
               tempArr[k] = arr[j++];
           }
           k++;
       }

       //If any element left from the first list.
       while(i<=m){
           tempArr[k++] = arr[i++];
       }

       //If any element left from the second list.
       while(j<=r){
        tempArr[k++] = arr[j++];
      }

      //Copying temp elements(from 'l' which is start to 'r' which is end) into main array
      int kM=0; //for temp array
      for(int iM=l;iM<=r;iM++){
          arr[iM] = tempArr[kM++];
      }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
          
        if(l<r){

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