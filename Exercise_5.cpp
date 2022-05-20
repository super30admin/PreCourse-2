
// Time Complexity : Average case O( n log(n) ) as each time the array gets divided into two parts ( log n ) and iteration of array cause the n times for each.
                     // worst case can be O( n*n ) but randomized pivot element can help in dividing the array into two almost equal halves. 
// Space Complexity : O(n) stack to store l and r of each subarray.
// Any problem you faced while coding this : None.
   // was able to figure out the use of stack.

// Your code here along with comments explaining your approach
/* Divide and conquer approach on array and on each iteration making the pivot element in correct position. Storing the l and r in each iteration to the stack for processing later. */

#include<iostream> 
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
    int pivot = h;
    int i = l;
    int index = l;
    while( i < pivot ){
       if( arr[i] < arr[pivot] ){
           swap( &arr[i], &arr[index]);
           index += 1;
       }
       i++;
    }
    swap( &arr[index], &arr[pivot] );
    return index;
}
  
/* A[] --> Array to be sorted,  
l --> Starting index,  
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) 
{ 
    //Try to think that how you can use stack here to remove recursion.
    if( l>=h ){  // still needed for one element in array so we dont do any unnecessary processing
        return;
    }
    stack<int>temp;
    int index = partition( arr, l, h );
    temp.push( l );
    temp.push( index-1 );
    temp.push( index+1 );
    temp.push( h );
    while( temp.size() ) {
     int end = temp.top(); 
     temp.pop();
     int start = temp.top();
     temp.pop();
     index = partition( arr, start, end );
     if( index-1 > start ){
        temp.push( start );
        temp.push( index-1 );
     }
     if( index+1 < end ){
         temp.push( index+1 );
         temp.push( end );
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
