// Time: O(n); Space: O(1)

#include <cstdio>

struct Node {
    int data;
    Node* next;
};

// For even lengths, the fast/slow traversal selects the second middle.
void printMiddle(Node* head)
{
    if (head == nullptr) {
        std::printf("The list is empty.\n");
        return;
    }

    Node* slow = head;
    Node* fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    std::printf("The middle element is %d\n", slow->data);
}

void push(Node** headRef, int newData)
{
    Node* newNode = new Node{newData, *headRef};
    *headRef = newNode;
}

void printList(Node* node)
{
    while (node != nullptr) {
        std::printf("%d->", node->data);
        node = node->next;
    }
    std::printf("NULL\n");
}

int main()
{
    Node* head = nullptr;
    for (int i = 15; i > 0; --i) {
        push(&head, i);
        printList(head);
        printMiddle(head);
    }
    return 0;
}
