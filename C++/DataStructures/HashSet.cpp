#include <iostream>
#include "HashSet.h"

int main() {
    HashSet<int> hashset;
    // Alternatively, using C++11 uniform initialization to call the default constructor:
    // HashSet<int> hashset{};
    // This could also be done with pointers and arrow operators, but there is no need.
    int arr[6] = {3, 2, 7, 6, 5, 3};

    // Test add, contains, containsValue
    hashset.add(arr[0]);
    std::cout << "Expected: 1\tActual: " << hashset.contains(arr[0]) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset.contains(arr[1]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset.contains(arr[5]) << std::endl;
    std::cout << std::endl;
    // Test add repeatedly with ints
    for (unsigned int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
        hashset.add(arr[i]);

    // Test add multiple strings
    // Note the hashset size is only 2 (and the one-arg constructor is called with the parentheses)
    HashSet<std::string> hashset2(2);
    std::string strs[] = {"trolling!abclol", "hello world", "Trolling", "This is the end of the world!", "Trolling"};
    // std::cout << sizeof(strs) << " " << sizeof(strs[0]) << " " << sizeof(std::string) << std::endl;
    for (unsigned int i = 0; i < sizeof(strs)/sizeof(strs[0]); i++)
        hashset2.add(strs[i]);
    
    // Test contains and containsValue with strings
    std::string str = "hello world";
    std::string str2 = "testing!"; // This value is not contained
    std::cout << "Expected: 1\tActual: " << hashset2.contains(strs[0]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset2.contains(str) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset2.contains(str2) << std::endl;
    std::cout << std::endl;

    // Test remove, removeValue, and output operator
    std::cout << hashset2 << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset2.remove(strs[0]) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset2.remove(strs[0]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset2.remove(str) << std::endl;
    std::cout << "Expected: 0\tActual: " << hashset2.remove(strs[1]) << std::endl;
    std::cout << "Expected: 1\tActual: " << hashset2.remove("Trolling") << std::endl;
    std::cout << "Expected:\t{ This is the end of the world! }" << std::endl;
    std::cout << "Actual:  \t" << hashset2 << std::endl;
    std::cout << std::endl;

    return 0;
}
