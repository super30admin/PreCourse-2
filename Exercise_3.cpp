// Time Complexity : O(N/2) ==> O(N)  
// Space Complexity : O(1)

#include <bits/stdc++.h>
using namespace std;

// Struct
struct Node
{
    int data;
    struct Node *next;
};

/* Function to get the middle of the linked list*/
void printMiddle(struct Node *head)
{
    // YourCode here
    // Use fast and slow pointer technique
    Node *slow = head, *fast = head;

    // iterate till fast pointer reaches last or last but one node
    while (fast != NULL && fast->next != NULL)
    {
        // move slow pointer by 1 unit
        slow = slow->next;

        // move fast pointer by 2 units
        fast = fast->next->next;
    }

    // print the middle node data
    cout << "Middle of the linkedlist:"
         << slow->data << endl;
}

// Function to add a new node
void push(struct Node **head_ref, int new_data)
{
    struct Node *new_node = new Node;
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
    struct Node *head = NULL;
    for (int i = 15; i > 0; i--)
    {
        push(&head, i);
        printList(head);
        printMiddle(head);
    }

    return 0;
}