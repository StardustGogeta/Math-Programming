#pragma once
#include <stdexcept>
#include <functional> // Used for std::hash
//#include <iostream>
#include "LinkedList.h"

/*
    This is a generic-type set that uses a hash table to store pointers to unique values.
    The set uses bucket hashing to allow for hash collisions without issues.
    Duplicate keys are compared using value comparison (and the value is how they are hashed),
    as opposed to using the memory addresses, themselves.
    Member functions:
        void add(T*)
        bool contains(T*)
        bool containsValue(T&)
        bool remove(T*)
*/
template <typename T>
class HashSet {
    public:
        // Adds element into the set (note that it uses value comparison to check for duplicates)
        // Throws std::invalid_argument if data pointer is null
        void add(T* data) {
            if (data == nullptr)
                throw std::invalid_argument("Invalid null argument in HashSet::add(T*)");
            int index = hashFunction(*data);
            if (table[index] == nullptr)
                table[index] = new LinkedList<T>;
            if (!table[index] -> containsValue(*data))
                table[index] -> prepend(data);
            // For debugging purposes, you can watch data as it is entered into buckets: (note the iostream requirement)
            // std::cout << "table[" << index << "] = " << table[index] << std::endl;
        }

        // Removes element by pointer from the set if possible (note that it STILL uses value comparison) and returns whether or not it was successful
        // Throws std::invalid_argument if data pointer is null
        bool remove(T* data) {
            if (data == nullptr)
                throw std::invalid_argument("Invalid null argument in HashSet::remove(T*)");
            return removeValue(*data);
        }

        // Removes element by value from the set if possible (note that it uses value comparison) and returns whether or not it was successful
        bool removeValue(T& data) {
            int index = hashFunction(data);
            if (table[index] == nullptr)
                return false;
            return table[index] -> removeValue(data);
        }

        // Checks for element in the set (pointer comparison)
        // Throws std::invalid_argument if data pointer is null
        bool contains(T* data) {
            if (data == nullptr)
                throw std::invalid_argument("Invalid null argument in HashSet::contains(T*)");
            int index = hashFunction(*data);
            if (table[index] == nullptr)
                return false;
            return table[index] -> contains(data);
        }

        // Checks for element in set (value comparison)
        bool containsValue(T& data) {
            int index = hashFunction(data);
            if (table[index] == nullptr)
                return false;
            return table[index] -> containsValue(data);
        }

        // Constructs hashtable of given input size
        // Throws std::out_of_range if hashtable size is nonpositive
        HashSet(int s = 1000) : hashTableSize(s) {
            if (s <= 0)
                throw std::out_of_range("Invalid hashtable size in HashSet::HashSet(int)");
            // The parentheses at the end of the line remove preexisting garbage values and prevent errors
            table = new LinkedList<T>*[s]();\
        }

        ~HashSet() {
            for (int i = 0; i < hashTableSize; i++)
                delete table[i];
            delete[] table;
        }

    private:
        int hashTableSize;
        LinkedList<T> **table;
        // Use the standard hash function utility
        std::hash<T> stdHash;
        int hashFunction(T& data) {
            return stdHash(data) % hashTableSize;
        }
        template <typename S>
        friend std::ostream& operator<<(std::ostream&, const HashSet<S>&);
};

template <typename S>
std::ostream& operator<<(std::ostream& os, const HashSet<S>& set) {
    os << "{ ";
    LinkedList<S> *ls;
    for (int i = 0; i < set.hashTableSize; i++) {
        ls = set.table[i];
        if (ls != nullptr) {
            int len = ls -> length();
            for (int j = 0; j < len; j++) {
                os << *(ls -> get(j));
                if (j < len - 1)
                    os << ", ";
            }
        }
        if (i < set.hashTableSize - 1)
            os << ", ";
    }
    os << " }";
    return os;
}

template <typename S>
std::ostream& operator<<(std::ostream& os, const HashSet<S>* set) {
    os << *set;
    return os;
}
