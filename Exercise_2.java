import java.util.Arrays;
//time complexity is O(n2)
//space complexity is O(n)
class QuickSort
{
    //utility method to swap two elements in an array
   static void swap(int arr[],int i,int j){
        int tmp =  arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;


    }

  /* partition method to partition the array in two halves with last element as pivot
    places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot*/
   static int partition(int arr[], int low, int high)
    { 
    int pivot = arr[high];

    int i =  (low-1);

    for(int j =low; j<= high -1; j++) {
     if(arr[j] < pivot) {
         i++;
         swap(arr, i , j);
     }
    }
    swap(arr, i+1, high);
    return  (i+1);
    }

    //sorts the elements in the array
   static void sort(int arr[], int low, int high)
    {  
          if(low < high) {
              int partitionIndex = partition(arr, low, high);
              sort(arr, low, partitionIndex -1);
              sort(arr, partitionIndex + 1, high);
          }
    }
     //prints the sorted array
    static void printArray(int arr[]) 
    {
        Arrays.stream(arr).forEach(System.out::print);
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
