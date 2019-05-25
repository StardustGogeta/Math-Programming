#pragma once
#include <stdexcept>
#include <ostream>

/*
    This is a generic-type linked list implemented with a dummy head node.
    Member functions:
        T* get(int)
        void append(T*)
        void prepend(T*)
        T* remove(int)
        void insert(int, T*)
        int length()
*/
template <typename T>
class LinkedList {
    public:
        // Returns pointer to data element at given index
        T* get(int index) {
            if (index < 0 || index >= len) {
                throw std::out_of_range("Invalid index in LinkedList::get(int)");
            }
            Node *ptr = Head -> next;
            for (; index-- > 0 ;)
                ptr = ptr -> next;
            return ptr -> data;
        }

        // Appends element to the end of the list
        void append(T* data) {
            insert(len, data);
        }

        // Prepends element to the start of the list
        void prepend(T* data) {
            insert(0, data);
        }

        // Removes element at a given index and returns a pointer to it
        T* remove(int index) {
            if (index < 0 || index >= len)
                throw std::out_of_range("Invalid index in LinkedList::get(int)");
            Node *ptr = Head;
            for (; index-- > 0 ;)
                ptr = ptr -> next;
            T* ret = ptr -> next -> data;
            ptr -> next = ptr -> next -> next;
            len--;
            return ret;
        }

        // Inserts element at a given index
        void insert(int index, T* data) {
            if (index < 0 || index > len)
                throw std::out_of_range("Invalid index in LinkedList::insert(int, T*)");
            if (data == nullptr)
                throw std::invalid_argument("Invalid null argument in LinkedList::insert(int, T*)");
            Node *ptr = Head;
            for (; index-- > 0 ;)
                ptr = ptr -> next;
            ptr -> next = new Node(data, ptr -> next);
            len++;
        }

        // Returns whether or not the list contains a certain object (pointer comparison)
        bool contains(T* data) {
            Node *ptr = Head -> next;
            while (ptr != nullptr) {
                if (ptr -> data == data)
                    return true;
                ptr = ptr -> next;
            }
            return false;
        }

        // Returns whether or not the list contains a certain object (value comparison)
        bool containsValue(T& data) {
            Node *ptr = Head -> next;
            while (ptr != nullptr) {
                if (*(ptr -> data) == data) {
                    return true;
                }
                ptr = ptr -> next;
            }
            return false;
        }

        // Returns the length of the list
        int length() {
            return len;
        }

        /*
            Safely deletes the allocated nodes (note that this does
            not delete the associated data, just the nodes themselves)
        */
        ~LinkedList() {
            Node *ptr = Head, *next;
            while (ptr != nullptr) {
                next = ptr -> next;
                delete ptr;
                ptr = next;
            }
        }

    private:
        class Node { public:
            T* data;
            Node *next;
            Node(T* data, Node* next = nullptr) {
                this -> data = data;
                this -> next = next;
            }
        };
        int len = 0;
        // Dummy head node
        Node *const Head = new Node(nullptr);
        template <typename S>
        friend std::ostream& operator<<(std::ostream&, const LinkedList<S>*);
};

template <typename S>
std::ostream& operator<<(std::ostream& os, const LinkedList<S>* ls) {
    os << "[ ";
    typename LinkedList<S>::Node *ptr = ls -> Head -> next, *next;
    while (ptr != nullptr) {
        os << *(ptr -> data);
        next = ptr -> next;
        if (next != nullptr)
            os << ", ";
        ptr = next;
    }
    os << " ]";
    return os;
}

