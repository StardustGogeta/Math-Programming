#include <stdio.h>
#include <stdlib.h> // Allow memory allocation
#include <math.h>
#include <stdint.h>

// Define a Node structure that holds an int and a pointer to the next Node
typedef struct Node {
    int val;
    struct Node *next; // You must have a pointer here, and you must you the `struct` keyword
} Node; // This allows you to write `Node` or `struct Node` as the type

// Construct a new valid Node and allocate memory
Node *newNode(int val) {
    Node *ret = malloc(sizeof(Node));
    ret -> val = val;
    ret -> next = NULL;
    return ret;
}

// Define a LinkedList that has a pointer to its head element
typedef struct LinkedList {
    Node *head;
} LinkedList;

// Construct a new LinkedList
LinkedList *newList() {
    LinkedList *ret = malloc(sizeof(LinkedList));
    ret -> head = NULL;
    return ret;
}

// Add a new Node to the end of a LinkedList
void addToList(LinkedList *list, Node *node) {
    Node *curr = list -> head;
    Node *prev = NULL;
    while (curr != NULL) {
        // printf("\nMemory Address: %d\n", curr);
        prev = curr;
        curr = curr -> next;
    }
    if (prev == NULL) // Head element
        list -> head = node;
    else // Standard append operation
        prev -> next = node;
    // printf("\nNew Value: %d\n", prev -> next -> val);
}

// Find the maximum element in a linked list
int listMax (LinkedList *list) {
    Node *curr = list -> head;
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

int main() {
    LinkedList *myList = newList();
    // You can manually set the head, or just start adding elements
    // myList -> head = newNode(501);
    addToList(myList, newNode(45));
    addToList(myList, newNode(-66));
    addToList(myList, newNode(3));
    addToList(myList, newNode(30));
    printf("The number %d is my maximum value.\n", listMax(myList));
    return 0;
}
