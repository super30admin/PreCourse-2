#include <iostream>
#include<stack>
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
    int pivot_index = l;
    for(int i=l;i<h;i++) {
        if (arr[i] <= pivot)
            swap(&arr[pivot_index++], &arr[i]);
    }

    swap(&arr[pivot_index], &arr[h]);
    return pivot_index;
}

/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h)
{
    //Try to think that how you can use stack here to remove recursion.

    stack <int> quick_sort_stack;
    quick_sort_stack.push(l);
    quick_sort_stack.push(h);

    while(!quick_sort_stack.empty()){
        h = quick_sort_stack.top();
        quick_sort_stack.pop();
        l = quick_sort_stack.top();
        quick_sort_stack.pop();
        int pi = partition(arr,l,h);

        if(pi-1>l){
            quick_sort_stack.push(l);
            quick_sort_stack.push(pi-1);
        }
        if(pi+1<h){
            quick_sort_stack.push(pi+1);
            quick_sort_stack.push(h);

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
