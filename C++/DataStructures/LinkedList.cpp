#include <iostream>
#include <iterator>
#include "LinkedList.h"
// Note that this file uses features from the C++17 standard, namely std::size.

int main() {
    LinkedList<int> *L = new LinkedList<int>;
    // This can be done without pointers, too:
    // LinkedList<int> L2;

    // Test append head
    int *x = new int(3);
    /* As an alternative,
    int y = 3;
    int *x = &y;
    */
    L -> append(x);
    // L2.append(x);
    std::cout << "Expected: 3\tActual: " << *(L->get(0)) << std::endl << std::endl;
    // std::cout << "Expected: 3\tActual: " << *(L2.get(0)) << std::endl << std::endl;

    // Test repeated append
    int arr[] = {45, 10, 32, 12, 11, 12, 1, -1, 0, 56};
    for (unsigned int i = 0; i < std::size(arr); i++)
        L -> append(arr + i);
    for (unsigned int i = 0; i < std::size(arr); i++)
        std::cout << "Expected: " << arr[i] << "\tActual: " << *(L->get(i+1)) << std::endl;
    std::cout << std::endl;

    // Test remove and length
    x = L -> remove(3);
    std:: cout << "Expected: 32\tActual: " << *x << std::endl;
    int newArr[] = {3, 45, 10, 12, 11, 12, 1, -1, 0, 56};
    for (int i = 0; i < L -> length(); i++)
        std::cout << "Expected: " << newArr[i] << "\tActual: " << *(L->get(i)) << std::endl;
    std::cout << std::endl;

    // Test insert and prepend
    L -> prepend(arr);
    L -> insert(1, arr + 1);
    for (int i = 0; i < 2; i++)
        std::cout << "Expected: " << arr[i] << "\tActual: " << *(L->get(i)) << std::endl;

    // Test contains
    std::cout << "Expected: 1\tActual: " << L -> contains(arr + 1) << std::endl;
    std::cout << "Expected: 0\tActual: " << L -> contains(arr + 2) << std::endl;
    std::cout << "Expected: 1\tActual: " << L -> contains(arr + 3) << std::endl;
    int *y = new int(12);
    std::cout << "Expected: 0\tActual: " << L -> contains(y) << std::endl; // Note the value of y is contained, but y itself is not
    std::cout << std::endl;

    // Test containsValue
    std::cout << "Expected: 1\tActual: " << L -> containsValue(arr[1]) << std::endl;
    std::cout << "Expected: 0\tActual: " << L -> containsValue(arr[2]) << std::endl;
    std::cout << "Expected: 1\tActual: " << L -> containsValue(arr[3]) << std::endl;
    std::cout << "Expected: 1\tActual: " << L -> containsValue(*y) << std::endl; // Note the difference from before
    std::cout << std::endl;

    delete L;
    return 0;
}
