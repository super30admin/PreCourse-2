// Time Complexity : O(nlogn)  avg. and O(n^2) in worst case
// Space Complexity : O(1)  

/*
In this type of Quicksort, instead of calling QuickSort recursively, low and high for each
subarray after partition are stored in a stack and then used for partitioning.

Recursive quicksort involves function calls to partition sub-arrays. 
These function calls can lead to overhead associated with managing the call stack, 
especially for large datasets. 
Iterative quicksort eliminates this overhead by using a loop to simulate the recursive calls, 
potentially improving performance.
*/


#include<iostream>
#include<vector>

using namespace std; 
    
/* This function is same in both iterative and recursive*/
int partition(std::vector<int> &arr, int low, int high) 
{ 
    //Do the comparison and swapping here 
    int i = low;
    int pivot = arr[high];
    
    for(int j=low; j<high; j++){
        if(arr[j] < pivot){
            std::swap(arr[j], arr[i]);
            i++;
        }
    }
    std::swap(arr[i], arr[high]);
    return i;
} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(std::vector<int> &arr, int low, int high) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    int stack[high-low+1];
    int top = -1;
    
    stack[++top] = low;
    stack[++top] = high;
    
    while(top>=0){
        int end = stack[top--];
        int start = stack[top--];
        int pi = partition(arr, start, end);
        //Check if elements are present of left of pi
        if(pi-1>low){
            stack[++top] = low;
            stack[++top] = pi-1;
        }
        //Check if elemets are presnet in right of pi
        if(pi+1<high){
            stack[++top] = pi+1;
            stack[++top] = high;
        }
    }
} 
  
// A utility function to print contents of arr 
void printArr(std::vector<int> &arr, int n) 
{
    int i; 
    for (i = 0; i < n; ++i) 
        std::cout << arr[i] << " "; 
} 
  
// Driver code 
int main() 
{ 
    std::vector<int> arr{9,3,5,7,6,2,1};
    quickSortIterative(arr, 0, arr.size()-1);
    printArr(arr, arr.size()); 
    return 0; 
} 