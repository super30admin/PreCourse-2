#include<stack>
#include <iostream>
using namespace std; 

// TC: O(nlogn) for best case, O(n^2) for worst case
// SC: O(n);

  
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
    int j = h;int i = l-1;
    while(i<j)
    {
        do{
            i++;
        }while(arr[i]<pivot);
        do{
            j--;
        }while(arr[j]>pivot);
        if(i<j){
            swap(arr[j],arr[i]);
        }
    }
    // cout << "pivot is :"<< pivot << " and arr[high] is : "<< arr[high]<< endl;
    swap(arr[i],arr[h]);
    return i;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    stack<int>st;
    st.push(l);
    st.push(h);

    while(!st.empty())
    {
        int h = st.top();
        st.pop();
        int l = st.top();
        st.pop();
        
        int p = partition(arr,l,h);

        if(p-1>l){
            st.push(l);
            st.push(p-1);
        }
        if(p+1<h){
            st.push(p+1);
            st.push(h);
        }
    }

} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; i++) 
        cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
    int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    quickSortIterative(arr, 0, n - 1); 
    cout << "Sorted array: \n"; 
    printArr(arr, n); 
    return 0; 
} 