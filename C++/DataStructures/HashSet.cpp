#include <iostream>
#include "HashSet.h"

int main() {
    HashSet<int> hashset;
    int arr[6] = {3, 2, 7, 6, 5, 3};
    hashset.add(arr);
    std::cout << "Expected: 1\tActual: " << hashset.contains(arr) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset.contains(arr + 5) << std::endl; // Note the value
    std::cout << "Expected: 1\tActual: " << hashset.containsValue(arr[0]) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset.containsValue(arr[1]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset.containsValue(arr[5]) << std::endl;

    // Write HashSet destructor and use it here!
    return 0;
}
