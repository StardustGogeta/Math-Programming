#include <stdio.h>
#include <stdlib.h> // Allow memory allocation
#include <stdbool.h> // Allow booleans
#include <math.h>
#include <stdint.h>

// Define a Node structure that holds an int and a pointer to the next Node
typedef struct Node {
    int val;
    struct Node *next; // You must have a pointer here, and you must use the `struct` keyword
} Node; // This allows you to write `Node` or `struct Node` as the type

// Construct a new valid Node and allocate memory
Node *newNode(int val) {
    Node *ret = malloc(sizeof(Node));
    ret -> val = val;
    ret -> next = NULL;
    return ret;
}

// Define a LinkedList that stores int values
typedef struct LinkedList {
    Node *head;
    int length;
    int (*max)(struct LinkedList *self);
    int (*get)(struct LinkedList *self, int index);
    void (*add)(struct LinkedList *self, int val);
    bool (*insert)(struct LinkedList *self, int index, int val);
} LinkedList;

// Find the maximum element in a linked list
int LinkedList_max (LinkedList *self) {
    Node *curr = self -> head;
    if (curr == NULL)
        return -1; // Empty list!
    int max = curr -> val, currVal;
    while (curr -> next != NULL) {
        // printf("\nMemory address: %d\n", curr);
        curr = curr -> next;
        currVal = curr -> val;
        if (currVal > max)
            max = currVal;
        // printf("CurrVal: %d\tMax: %d\n", currVal, max);
    }
    return max;
}

// Find the element at a certain index in a linked list
int LinkedList_get (LinkedList *self, int index) {
    Node *curr = self -> head;
    if (curr == NULL || index < 0)
        return -1; // Empty list or index out of bounds!
    while (index-- > 0 && curr != NULL)
        curr = curr -> next;
    if (curr == NULL)
        return -2; // Index out of bounds!
    return curr -> val;
}

// Add an element to a linked list
void LinkedList_add (LinkedList *self, int val) {
    Node *node = newNode(val);
    Node *curr = self -> head;
    Node *prev = NULL;
    while (curr != NULL) {
        // printf("\nMemory Address: %d\n", curr);
        prev = curr;
        curr = curr -> next;
    }
    if (prev == NULL) // Head element
        self -> head = node;
    else // Standard append operation
        prev -> next = node;
    // printf("\nNew Value: %d\n", prev -> next -> val);
    self -> length++;
}

// Add an element to a linked list
bool LinkedList_insert (LinkedList *self, int index, int val) {
    Node *node = newNode(val);
    Node *curr = self -> head;
    if (index == 0) { // Head element
        Node *temp = self -> head;
        self -> head = node;
        node -> next = temp;
    }
    else {
        if (curr == NULL || index < 0)
            return false; // Empty list or index out of bounds!
        while (index-- > 1 && curr -> next != NULL)
            curr = curr -> next;
        if (curr -> next == NULL) {
            if (index > 1)
                return false; // Index out of bounds!
            curr -> next = node;
        }
        else {
            Node *temp = curr -> next;
            curr -> next = node;
            node -> next = temp;
        }
    }
    self -> length++;
    return true;
}

// Construct a new LinkedList
LinkedList *newLinkedList() {
    LinkedList *ret = malloc(sizeof(LinkedList));
    ret -> head = NULL;
    ret -> length = 0;
    ret -> max = &LinkedList_max;
    ret -> get = &LinkedList_get;
    ret -> add = &LinkedList_add;
    ret -> insert = &LinkedList_insert;
    return ret;
}

int main() {
    LinkedList *myList = newLinkedList();

    // You can manually set the head, or just start adding elements
    // myList -> head = newNode(501);
    myList->add(myList, 45);
    myList->add(myList, -66);
    myList->add(myList, 3);
    myList->add(myList, 30);
    myList->insert(myList, 0, 10);
    myList->insert(myList, 3, 1);
    myList->insert(myList, 6, 50);
    myList->insert(myList, 0, 432);

    printf("The number %d is my maximum value.\n\n", myList->max(myList));

    for (int i = 0; i < myList->length; i++) {
            printf("Index %d : %d\n", i, myList->get(myList, i));
    }

    return 0;
}
