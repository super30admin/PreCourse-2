// Time Complexity : O(n log n)
// Space Complexity : Not sure
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : Yes, I was not sure how to implement it and I refereed few videos but still i was unable to do it on my own

class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){             //Swap logic to swap two elements using a temp variable
        //Your code here   
        int temp = arr[i];
        arr[i]= arr[j];
        arr[j]=temp;
    }
    
    int partition(int arr[], int low, int high)        //this is a partition function which compares every element with the pivot and places small elements than pivot at left and greater elements to the right of pivot and returns pivot
    { 

        int pivot = arr[high];
        int x=low-1;                                    //x is the pointer which we are maintaining and it will return the correct position of the pivot

        for(int i=low;i<high;i++){                      //the loop will be low to high and then at the end we will swap the pivot
            if(arr[i]<pivot){
                x++;
            swap(arr,x,i);
            }
        }
        x++;
        swap(arr,x,high);
        return x;


   	//Write code here for Partition and Swap 
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high)                       //This is the sort function which is recursively called based on the pivot.
    {                                                             //for example if there are 10 elements and pivot is the sixth element then sort function will be recursively called for 0 to 5 index and 7-10 element and so on.

        if(low<high){                                              
            int pivotIndex = partition(arr,low,high);           //pivotIndex will be the index of the pivot
            sort(arr,low,pivotIndex-1);
            sort(arr,pivotIndex+1,high);
        }   
            // Recursively sort elements before 
            // partition and after partition 
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
