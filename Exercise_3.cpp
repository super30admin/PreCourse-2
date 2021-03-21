#include<bits/stdc++.h>  
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
    Node *hare = head, *turtle = head;

    while ((nullptr != hare) && (nullptr != hare->next)) {
        hare = hare->next->next;
        turtle = turtle->next;
    }

    cout << "Middle node is " << turtle->data << endl;
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
    while (nullptr != ptr) {
        cout << ptr->data << "->";  
        ptr = ptr->next;
    }

    cout << "NULL" << endl;
}  
  
// Driver Code 
int main()  
{    
    struct Node* head = nullptr;

    for (int i = 15; i > 0; i--) {
        push(&head, i);  
        printList(head);  
        printMiddle(head);  
    }

    return 0;
}
