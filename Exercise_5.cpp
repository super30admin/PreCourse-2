#include <bits/stdc++.h> 
using namespace std; 

//Time - O(n log n) n is the size of the input array;
//Space - O(n) Stack used to store l & h

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
    int pivotElem = arr[h];
    int i = l-1;
    for(int j = l;j<h;j++){
        if(arr[j]<pivotElem){
            i++;
            swap(&arr[i],&arr[j]);
        }
    }
    swap(&arr[i+1],&arr[h]);
    return i+1;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int> s;
    s.push(l);
    s.push(h);
    while(s.size()){
        h = s.top(); 
        s.pop();
        l = s.top();
        s.pop();
        int part = partition(arr,l,h);
        if(part-1>l){
            s.push(l);
            s.push(part-1);
        }
        if(part+1<h){
            s.push(part+1);
            s.push(h);
        }
    }
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " ";
    cout<<endl;
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