#include <bits/stdc++.h> 
#include <stack>
using namespace std;  


//TC: Average - O(nlog n), Worst - O(n^2)
//SC: O(log n)  


// A utility function to swap two elements  
void swap(int* a, int* b)  
{  
    int temp = *a;
    *a =*b;
    *b = temp;
    //Your Code here 

}  
  
/* This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot */
int partition (int arr[], int low, int high)  
{  
  //set pivot as last element here.
  int pivot = arr[high];

  int i = low-1;
  
  for(int j = low; j<=high; j++){
    if(arr[j] < pivot)
    {
      i++;
      swap(&arr[j], &arr[i]);
    }
  }

  swap(&arr[i+1], &arr[high]);

  return i+1;

    //Your Code here 
}  
  
/* The main function that implements QuickSort  
arr[] --> Array to be sorted,  
low --> Starting index,  
high --> Ending index */
void quickSort(int arr[], int low, int high)  
{  
    stack<int> s;
    s.push(low);
    s.push(high);

    while(!s.empty()){

      int h = s.top(); s.pop();
      int l = s.top(); s.pop();

      int piv = partition(arr, l, h);

      if(piv - 1 > l) {
        s.push(l);
        s.push(piv-1);
      }

      if(piv + 1 < h){
        s.push(piv+1);
        s.push(h);
      }
    }


    //Your Code here 
}  
  
/* Function to print an array */
void printArray(int arr[], int size)  
{  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  
  
// Driver Code 
int main()  
{  
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quickSort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;  
}  