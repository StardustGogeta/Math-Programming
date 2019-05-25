#include <iostream>
#include "HashSet.h"

int main() {
    HashSet<int> hashset;
    // Alternatively, using C++11 uniform initialization to call the default constructor
    // HashSet<int> hashset{};
    int arr[6] = {3, 2, 7, 6, 5, 3};

    // Test add
    hashset.add(arr);
    std::cout << "Expected: 1\tActual: " << hashset.contains(arr) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset.contains(arr + 5) << std::endl; // Note the value
    std::cout << "Expected: 1\tActual: " << hashset.containsValue(arr[0]) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset.containsValue(arr[1]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset.containsValue(arr[5]) << std::endl;
    // Test add repeatedly with ints
    for (unsigned int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
        hashset.add(arr + i);

    // Test add multiple strings
    // Note the hashset size is only 2 (and the one-arg constructor is called with the parentheses)
    HashSet<std::string> hashset2(2);
    std::string strs[] = {"trolling!abclol", "hello world", "Trolling", "This is the end of the world!", "Trolling"};
    // std::cout << sizeof(strs) << " " << sizeof(strs[0]) << " " << sizeof(std::string) << std::endl;
    for (unsigned int i = 0; i < sizeof(strs)/sizeof(strs[0]); i++)
        hashset2.add(strs + i);

    // Write HashSet destructor and use it here!
    return 0;
}
