#pragma once
#include <stdexcept>
#include <functional>
#include "LinkedList.h"

// Generic-type set that uses a hash table to store values
// The set uses bucket hashing to allow for duplicate keys without issues
template <typename T>
class HashSet {
    public:
        // Adds element into the set
        void add(T* data) {
            int index = hashFunction(*data);
            if (table[index] == nullptr) {
                table[index] = new LinkedList<T>;
            }
            table[index] -> append(data);
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
            table = new LinkedList<T>*[s];
        }

    private:
        int hashTableSize = 1000;
        LinkedList<T> **table;
        // Use the standard hash function utility
        std::hash<T> stdHash;
        int hashFunction(T& data) {
            return stdHash(data) % hashTableSize;
        }
};
