#include <iostream>

int main() {
    // Read in the number of levels
    int n;

    std::cin >> n;

    // Print the staircase
    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < n - i; j++) {
            std::cout << " ";
        }

        for (int k = 0; k < i; k++) {
            std::cout << "#";
        }

        std::cout << std::endl;
    }

    return 0;
}
