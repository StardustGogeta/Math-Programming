#pragma once
#include <stdexcept>
#include <functional> // Used for std::hash
//#include <iostream>
#include "LinkedList.h"

/*
    This is a generic-type set that uses a hash table to store unique values.
    The set uses bucket hashing to allow for hash collisions without issues.
    Member functions:
        void add(const T&)
        bool contains(const T&) const
        bool remove(const T&)
*/
template <typename T>
class HashSet {
    public:
        // Adds element into the set
        void add(const T& data) {
            int index = hashFunction(data);
            if (!table[index]) // No bucket present
                table[index] = new LinkedList<T>; // Create bucket
            if (!table[index] -> contains(data)) // Value not present already
                table[index] -> prepend(data); // Adding value

            // For debugging purposes, you can watch data as it is entered into buckets: (note the iostream requirement)
            // std::cout << "table[" << index << "] = " << table[index] << std::endl;
        }

        // Removes element from the set, if possible, and returns whether or not it was successful
        bool remove(const T& data) {
            int index = hashFunction(data);
            return table[index] && table[index] -> removeValue(data);
        }

        // Checks for element in the set
        bool contains(const T& data) const {
            int index = hashFunction(data);
            return table[index] && table[index] -> contains(data);
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
        int hashFunction(const T& data) const {
            return stdHash(data) % hashTableSize;
        }
        template <typename S>
        friend std::ostream& operator<<(std::ostream&, const HashSet<S>&);
};

template <typename S>
std::ostream& operator<<(std::ostream& os, const HashSet<S>& set) {
    os << "{ ";
    for (int i = 0; i < set.hashTableSize; i++) {
        LinkedList<S> *ls = set.table[i];
        if (ls) {
            int len = ls -> length();
            for (int j = 0; j < len; j++) {
                os << ls -> get(j);
                if (j < len - 1)
                    os << ", ";
            }
            if (len > 0 && i < set.hashTableSize - 1)
                os << ", ";
        }
    }
    os << " }";
    return os;
}
