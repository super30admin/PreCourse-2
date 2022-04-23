// Time Complexity : O(N*logN)
// Space Complexity : O(logN)
class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp; 
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	  	//Write code here for Partition and Swap 
       //Create an int variable pivot that holds last element of the array
       int pivot = arr[high];
       //Create an int variable l=> leftpointer that holds low value
       int l=low;
       //Create an int variable r=>rightpointer that holds high-1 value
       int r=high - 1;
       //Loop till both the pointers overlap
       while(l < r){
           //if arr[l] less than or equal to pivot element 
           while(arr[l] <= pivot && l<r){
            //move the pointer forward to next element in the array
               l++;
           }
            //if arr[h] greater than or equal to pivot element 
           while(arr[r] >= pivot && l<r){
            //move the pointer forward to left of element in the array 
               r--;
           }
       //swap arr[l] and arr[r] elements 
       swap(arr,l,r);
        }
        //If last element is out of order if so then swap arr[l] and arr[high]
        if(arr[l]>arr[high]){
            swap(arr,l,high);
        }
        //Else assign high to l 
        else{
            l=high;
        }
        //Return leftpointer
        return l;
    } 
    
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
           //If starting index is greater than ending index or equal to it then simply return as the array is sorted
        if(low >=high){
            return;
        }
        if(low < high){
            //Create and int variable r which takes the int value returned by partition()
            int r = partition(arr, low, high);
            //Recursively sort elements before
            //Partition and after partition 
            //Sort first half
            sort(arr,low,r-1);
            //Sort second half
            sort(arr,r+1,high);
        }
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
