#include<bits/stdc++.h>  
using namespace std;  
  
/*
Time Complexity :
    printMiddle(): O(n/2) ~ O(n), n is the number of elements in the array

Space Complexity : O(1) - no extra set of datastructure used

Did this code successfully run on Leetcode : Couldn't find the leetcode problem

Any problem you faced while coding this : None
*/

// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  
  
/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)  
{  
  //YourCode here
  //Use fast and slow pointer technique
    Node* slow = head;
    Node* fast = head;

    while (fast -> next != NULL && fast -> next -> next != NULL) {
        slow = slow -> next;
        fast = fast -> next -> next;
    }

    printf("%d\n", slow -> data);
}  
  
// Function to add a new node  
void push(struct Node** head_ref, int new_data)  
{  
    struct Node* new_node = new Node;  
    new_node->data = new_data;  
    new_node->next = (*head_ref);  
    (*head_ref) = new_node;  
}  
  
// A utility function to print a given linked list  
void printList(struct Node *ptr)  
{  
    while (ptr != NULL)  
    {  
        printf("%d->", ptr->data);  
        ptr = ptr->next;  
    }  
    printf("NULL\n");  
}  
  
// Driver Code 
int main()  
{    
    struct Node* head = NULL;    
    for (int i=15; i>0; i--)  
    {  
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }  
  
    return 0;  
}  