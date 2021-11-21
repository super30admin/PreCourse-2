#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;
// Time complexity --> O(Logn)
// Space Complexity --> O(1)
// Struct
struct Node
{
    int data;
    struct Node* next;
};

/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)
{
    Node * fast = head;
    Node * slow = head;//14
    while(fast != NULL){
       fast = fast->next;
       if(fast != NULL){
           fast = fast->next;
       }
        if(fast != NULL){
            slow = slow->next;
        }
    }
    cout<<"The middle element is " <<slow->data<<endl;
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