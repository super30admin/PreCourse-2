// Time Complexity - I was unable to visualize what the time comlexity would be here for partition() and the quicksort().
// Problems faced - I had to refer various sources on google to undestand how stack/array can be used to implement quick sort in a recursive manner. I could not come up with the solution on my own.
// Also, my program fails to build when a negative number or a zero is present in the input array. I am pretty sure that my partition() function is causing this. I tried to debug but was not able to.
#include <bits/stdc++.h>
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
    int pivot = arr[h];
    int i = l; // left pointer
    int j = h; // right pointer
    
    // left pointer checks for elements greater than or equal to pivot. It stops as soon as it finds one.
    // right pointer checks for elements less than pivot. It stops as soon as it finds one.
    // if their search is successfull and at that point i is less than j, I swap those elements
    // if i > j it breaks out of the while loop and swaps pivot and arr[i]
    while(i < j){
        while(arr[i] < pivot)
            i++;
        do{
            j--;
        }while(arr[j] >= pivot);
        
        if(i < j)
            swap(&arr[i], &arr[j]);
    }
    
    swap(&arr[h], &arr[i]);
    return i;
}
  
/* A[] --> Array to be sorted,
l --> Starting index,
h --> Ending index */
void quickSortIterative(int arr[], int l, int h)
{
    //Try to think that how you can use stack here to remove recursion.
    // I used an array to implement an iterative algorithm for QuickSort.
    int a[h-l+1];
    int ptr = -1; // will be used as a pointer to index of array "a"
    a[++ptr] = l;
    a[++ptr] = h;
    
    while(ptr >= 0){
        h = a[ptr--];
        l = a[ptr--];
        
        int index = partition(arr, l, h);
        if(index - 1 > l){
            a[++ptr] = l;
            a[++ptr] = index - 1;
        }
        if(index + 1 < h){
            a[++ptr] = index + 1;
            a[++ptr] = h;
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
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 7, 90};
    //int arr[] = {5, 8, 7, 6};
    int n = sizeof(arr) / sizeof(*arr);
    quickSortIterative(arr, 0, n - 1);
    printArr(arr, n);
    return 0;
}
