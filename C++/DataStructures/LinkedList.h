#pragma once
#include <stdexcept>
#include <ostream>

/*
    This is a generic-type linked list implemented with a dummy head node that stores pointers to data.
    Member functions:
        void append(T*)
        bool contains(T*)
        bool containsValue(T&)
        T* get(int)
        void insert(int, T*)
        int length()
        void prepend(T*)
        T* remove(int)
        bool remove(T*)
        bool removeValue(T&)
*/
template <typename T>
class LinkedList {
    public:
        // Returns pointer to data element at given index
        // Throws std::out_of_range if index is invalid
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
        // Throws std::out_of_range if index is invalid
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

        // Removes element by pointer if found (using pointer comparison) and return whether or not it was successful
        // Throws std::invalid_argument if data pointer is null
        bool remove(T* data) {
            if (data == nullptr)
                throw std::invalid_argument("Invalid null argument in LinkedList::remove(T*)");
            Node *ptr = Head;
            while (ptr -> next != nullptr && ptr -> next -> data != data)
                ptr = ptr -> next;
            if (ptr -> next == nullptr)
                return false;
            ptr -> next = ptr -> next -> next;
            len--;
            return true;
        }

        // Removes element by value if found (using value comparison) and return whether or not it was successful
        bool removeValue(T& data) {
            Node *ptr = Head;
            while (ptr -> next != nullptr && *(ptr -> next -> data) != data)
                ptr = ptr -> next;
            if (ptr -> next == nullptr)
                return false;
            ptr -> next = ptr -> next -> next;
            len--;
            return true;
        }

        // Inserts element at a given index
        // Throws std::out_of_range if index is invalid
        // Throws std::invalid_argument if data pointer is null
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

template <typename S>
std::ostream& operator<<(std::ostream& os, const LinkedList<S>& ls) {
    os << &ls;
    return os;
}
