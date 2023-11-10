/*

// Time Complexity : O(N) cause going through complete list atleast N/2 times.
// Space Complexity : O(1) cause no new memory instance were created
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

*/


#include<iostream>
using namespace std;  
  
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

    if(!head)
    {
        cout<<"the linked list is empty "<<endl;
        return;
    }

    struct Node* slow = new Node;
    struct Node* fast = new Node;
    slow = head;
    fast = head;

    while(fast->next && (fast->next)->next)
    {
        slow = slow->next;
        fast = (fast->next)->next;
    }

    cout<<"The first middle element is "<<slow->data;

    //Use fast and slow pointer technique
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
        cout<<endl;  
    }  
  
    return 0;  
}  