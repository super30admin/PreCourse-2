// Time Complexity : O(nlogn)
// Space Complexity : O(logn)
class QuickSort 
{ 
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] =arr[j];
        arr[j] = temp;
    }

    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
    int partition(int arr[], int low, int high) 
    { 
        //selecting the end element as the pivot
        int pivot = arr[high];
        int i = low;//left pointer
        int j = high;//right pointer
        //iterate until the left pointer index is lesser than right pointer index indicating that all the elements are traversed
        while(i<j){
            //move the left pointer to the right until the element is greater than pivot
          while(arr[i]<=pivot && i<j){
              i++;
          }
          //move the right pointer to the left until the element is lesser than pivot
          while(arr[j]>=pivot && i<j){
              j--;
          }
          //swap the left pointer element and the right pointer element, thus maintaining the logic that all elements smaller than the pivot is to its left and all element
          //greater than the pivot is to it's right
          swap(arr, i, j);
        }
        //Finally swap the left pointer element with the pivot element, thus pivot element is now in its correct position
        swap(arr, high, i);
        //return the new pivot index
        return i;
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {  
            // Recursively sort elements before 
            // partition and after partition 
            //sort until atleast 2 elements are present in the subarrays
            if(low<high){
                //get the partition point such that the left subarray and right subarray of the partition index needs to be sorted
                int p = partition(arr, low, high);
                //recursively pass the left subarray from low index to p-1 through the sort function
                sort(arr, low, p-1);
                //recursively pass the right subarray from p+1 index to high index through the sort function
                sort(arr, p+1,high);
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
