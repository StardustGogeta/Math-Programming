#pragma once
#include <stdexcept>
#include <ostream>

/*
    This is a generic-type linked list implemented without using the C++ STL.
    Member functions:
        void append(const T&)
        bool contains(const T&) const
        T get(int) const
        void insert(int, const T&)
        int length() const
        void prepend(const T&)
        T remove(int)
        bool removeValue(const T&)
*/
template <typename T>
class LinkedList {
    public:
        // Appends element to the end of the list
        void append(const T& data) {
            insert(len, data);
        }

        // Returns data element at given index
        // Throws std::out_of_range if index is invalid
        T get(int index) const {
            if (index < 0 || index >= len)
                throw std::out_of_range("Invalid index in LinkedList::get(int)");
            Node *ptr = Head;
            // Traverse up to the matching node
            for (; index-- ;)
                ptr = ptr -> next;
            return ptr -> data;
        }

        // Prepends element to the start of the list
        void prepend(const T& data) {
            insert(0, data);
        }

        // Removes element at a given index, if possible, and returns it
        // Throws std::out_of_range if index is invalid
        T remove(int index) {
            if (index < 0 || index >= len)
                throw std::out_of_range("Invalid index in LinkedList::get(int)");
            Node *old;
            if (index == 0) { // Deleting the head
                old = Head; // Save the removed node to free later
                Head = Head -> next; // Skip over the node
            }
            else {
                Node *ptr = Head;
                for (; --index ;) // Traverse up to just before the matching node
                    ptr = ptr -> next;
                old = ptr -> next; // Save the removed node to free later
                ptr -> next = old -> next; // Skip over the node
            }
            T ret = old -> data; // Save the removed data to return later
            delete old; // Delete the node from memory
            len--;
            return ret;
        }

        // Removes element by value, if found, and return whether or not it was successful
        bool removeValue(const T& data) {
            Node *ptr = Head;
            if (!ptr) // Empty list
                return false;
            Node *old;
            if (ptr -> data == data) { // Deleting the head
                old = Head; // Save the removed node to free later
                Head = old -> next; // Skip over the node
            }
            else {
                // Advance until the end of the list, or just before the object is found
                while (ptr -> next && ptr -> next -> data != data)
                    ptr = ptr -> next;
                if (!ptr -> next) // End of the list
                    return false;
                // Object was found
                Node *old = ptr -> next; // Save the removed node to free later
                ptr -> next = old -> next; // Skip over the node
            }
            delete old; // Delete the node from memory
            len--;
            return true;
        }

        // Inserts element at a given index
        // Throws std::out_of_range if index is invalid
        void insert(int index, const T& data) {
            if (index < 0 || index > len)
                throw std::out_of_range("Invalid index in LinkedList::insert(int, T*)");
            if (index == 0)
                Head = new Node(data, Head);
            else {
                Node *ptr = Head;
                // Traverse up to one node prior to the insertion
                for (; --index ;)
                    ptr = ptr -> next;
                // std::cout << "HOLA " << index << " " << data << " " << len << " " << ptr << std::endl;
                ptr -> next = new Node(data, ptr -> next);
            }
            len++;
        }

        // Returns whether or not the list contains a given element
        bool contains(const T& data) const {
            Node *ptr = Head;
            while (ptr != nullptr) {
                if (ptr -> data == data)
                    return true;
                ptr = ptr -> next;
            }
            return false;
        }

        // Returns the length of the list
        int length() const {
            return len;
        }

        // Deletes all Nodes in the list
        ~LinkedList() {
            Node *ptr = Head, *next;
            // Iterate through the list
            while (ptr) {
                next = ptr -> next;
                delete ptr;
                ptr = next;
            }
        }

    private:
        class Node { public:
            const T data;
            Node *next;
            Node(const T& data, Node* next = nullptr) : data(data), next(next) { }
        };
        int len = 0;
        Node *Head = nullptr;
        template <typename S>
        friend std::ostream& operator<<(std::ostream&, const LinkedList<S>&);
};

template <typename S>
std::ostream& operator<<(std::ostream& os, const LinkedList<S>& ls) {
    os << "[ ";
    typename LinkedList<S>::Node *ptr = ls.Head, *next;
    // Iterate through the list
    while (ptr) {
        os << ptr -> data;
        next = ptr -> next;
        if (next) // If not at the end of the list
            os << ", ";
        ptr = next;
    }
    os << " ]";
    return os;
}
