#include <iostream> 
using namespace std; 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function is same in both iterative and recursive*/
int partition(int arr[], int l, int h) 
{ 
    //Do the comparison and swapping here 
        //Your Code here
        int i=l;
    int j=l;
    while(j<h){
        if(arr[i]<=arr[h]){
i++;
j++;
        }
        else{
            while(j<h && arr[j]>arr[h] ){
            j++;
            }
     
            if(j<h){
                swap(arr[i],arr[j]);
               i++;
            j++;
            }

        }

    }
    swap(arr[h],arr[i]);
    return i; 
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
  
    int pivot = partition(arr,l,h);
    int start = pivot+1;
    int end =h;
     h=pivot-1;
    while(l<h){
    

pivot = partition(arr,l,h);
h=pivot-1;
    }
   while(start<end){
    pivot = partition(arr,start,end);
start=pivot+1;
    }
    
    

} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
  int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(*arr); 
    quickSortIterative(arr, 0, n - 1); 
    printArr(arr, n); 
    return 0; 
} 