#pragma once
#include <stdexcept>
#include <functional>
//#include <iostream>
#include "LinkedList.h"

// Generic-type set that uses a hash table to store values
// The set uses bucket hashing to allow for hash collisions without issues
// Duplicate keys are compared using value comparison (and the value is how they are hashed),
// as opposed to using the memory addresses of the keys instead
template <typename T>
class HashSet {
    public:
        // Adds element into the set (note that it uses value comparison to check for duplicates)
        void add(T* data) {
            int index = hashFunction(*data);
            if (table[index] == nullptr)
                table[index] = new LinkedList<T>;
            if (!table[index] -> containsValue(*data))
                table[index] -> prepend(data);
            // For debugging purposes, you can watch data as it is entered into buckets: (note the iostream requirement)
            // std::cout << "table[" << index << "] = " << table[index] << std::endl;
        }

        // Checks for element in the set (reference comparison)
        bool contains(T* data) {
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
        HashSet(int s = 1000) : hashTableSize(s) {
            // The parentheses at the end of the line remove preexisting garbage values and prevent errors
            table = new LinkedList<T>*[s]();
        }

    private:
        int hashTableSize;
        LinkedList<T> **table;
        // Use the standard hash function utility
        std::hash<T> stdHash;
        int hashFunction(T& data) {
            return stdHash(data) % hashTableSize;
        }
};
