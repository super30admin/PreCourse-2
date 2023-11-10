class QuickSort{

public void sort(int[] arr){
  if(arr == null || arr.length == 0 ) return ;
  splitAndSort(arr, 0, arr.length-1);
}

public void sort(int[] arr, int low, int high){
  if(arr == null || arr.length == 0 ) return ;
  splitAndSort(arr, low, high);
}

public void splitAndSort(int[] arr, int low, int high){
  if(low >= high) return;
  int pivot = sortPivot(arr, 0, high);
  splitAndSort(arr, 0, pivot-1);
  splitAndSort(arr, pivot+1, high);
}

public int sortPivot(int[] arr, int low, int high){

  while(high > 0 &&low < high){

    if(arr[low] <= arr[high] ){
      low++;
    }
    else{
      int temp = arr[high];
      arr[high] = arr[low];
      arr[low] = arr[high-1];
      arr[high-1] = temp;
      high--;
    }
  }
  return high;
}
static void printArray(int arr[])
{
    int n = arr.length;
    for (int i=0; i<n; ++i)
        System.out.print(arr[i]+" ");
    System.out.println();
}



public static void main(String[] args){
//int[] arr = {7,6,5,11,13,2,4,8};
//int arr[] = {10, 7, 8, 9, 1, 5};
  //int arr[] = {12, 11, 13, 5, 6, 7};
    //int arr[] = {};
    //int arr[] = {1};
    //int arr[] = {12,11};

    //int arr[] = {1,2,3,4,5,6};

    int arr[] = {6,5,4,3,2,1};
    int n = arr.length;

QuickSort ob = new QuickSort();
ob.sort(arr, 0, n-1);

System.out.println("sorted array");
printArray(arr);



}
}
