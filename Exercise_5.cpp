#include <bits/stdc++.h> 
#include <stack>
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
    int pivot_index= h;
    int pivot_ele = arr[h];

    int i= l-1;

    for ( int j = l ; j<= h ; j++){
        if(arr[j] < pivot_ele){
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[h]); //placing pivot at correct place
    return (i+1);
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */

//Time complexity: O(nlogn)
//Space complexity: O(logn)
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack <int> s1;

    s1.push(l);
    s1.push(h);

    while( !s1.empty()){
        h= s1.top();
        s1.pop();
        l= s1.top();
        s1.pop();

        int p = partition(arr, l, h);

        if(p-1 >l ){
            s1.push(l);
            s1.push(p-1);
        }
        if(p+1 < h){
            s1.push(p+1);
            s1.push(h);
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