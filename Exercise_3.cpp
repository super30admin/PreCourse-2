#include<bits/stdc++.h>  
using namespace std;  
  
// Struct  
struct Node  
{  
    int data;  
    struct Node* next;  
};  

/* Function to get the middle of the linked list*/

// Time Complexity : O(n)
// Space Complexity : O(1)
void printMiddle(struct Node *head)  
{  
    //YourCode here
    //Use fast and slow pointer technique

    // Initialising fast pointer and slow pointer with the head of the list.
    struct Node *fast_ptr = head;
    struct Node *slow_ptr = head;
  
    if (head!=NULL)
    {
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            // Slow pointer moves forward by one node.
            slow_ptr = slow_ptr->next;

            // Fast pointer moves forward by 2 nodes.
            fast_ptr = fast_ptr->next->next;
            
        }
        cout << "The middle element is: " << slow_ptr->data << "\n\n";
    }
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