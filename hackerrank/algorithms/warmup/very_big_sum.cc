#include <iostream>

int main() {
    // Set up variables
    int64_t sum;
    std::string s;

    // Ignore the first line of input
    std::getline(std::cin, s, '\n');

    // Read in the numbers
    sum = 0;

    while (std::getline(std::cin, s, ' ')) {
        sum += std::stoll(s);
    }

    // Print answer
    std::cout << sum << std::endl;

    return 0;
}
