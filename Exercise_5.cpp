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
      int pivot = arr[l];
      int start = l;
      int end = h;

      while(start<end){
        while(arr[start]<=pivot){
            start++;
        }
        while(arr[end]>pivot){
            end--;
        }
        if(start<end){
            swap(&arr[start],&arr[end]);
        }
      }


      swap(&arr[l],&arr[end]);
      return end;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.


        int stack[h-l+1];
     int top =-1;

     stack[++top]=l;
     stack[++top]=h;

     while(top>0){
        h = stack[top--];
        l = stack[top--];

        int pi = partition(arr,l,h);

        if(pi-1>l){
            stack[++top] = l;
            stack[++top] = pi-1;
        }

        if(pi +1<h){
            stack[++top] = pi+1;
            stack[++top] = h;
        }
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