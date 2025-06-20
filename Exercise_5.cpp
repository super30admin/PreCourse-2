// Time Complexity :O(nlogn) avg
// Space Complexity :O(logn) - for stack to store partition indices
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


#include <iostream> 
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
    int pivot = arr[h];
    int i = l -1 ;
    for(int j = l; j <= h - 1; j++){
        if(arr[j] <= pivot){
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[h]);
    return (i+1);

} 
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */

//we just need low and high value sof the sub arrays to aplly partition instead of recursiv erule so,
void quickSortIterative(int arr[], int l, int h) 
{ 
    stack<int> stack; // creating a stack
    
    stack.push(l); //pushing low index to stack 
    stack.push(h); //pushing high index to stack

    while(!stack.empty()){//keep popping while stack is not empty
        h = stack.top();
        stack.pop();
        l = stack.top();
        stack.pop();

        int p  = partition(arr, l, h); // setting pivot at current location

        //if there are elements on the stack push the left indices to the stack
        if(l < p -1){
            stack.push(l);
            stack.push(p -1);
        }
        // if there are elemnts on the right side then push right indices on to the stack
        if(p + 1 < h){
            stack.push(p + 1);
            stack.push(h);
        }

    }

    //Try to think that how you can use stack here to remove recursion.
} 
  
// A utility function to print contents of arr 
void printArr(int arr[], int n) 
{ 
    int i; 
    for (i = 0; i < n; ++i) 
        cout << arr[i] << " "; 
    cout << endl;
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