#include <iostream>

int main() {
    // Read in the number of input numbers
    int n;

    std::cin >> n;

    // Count the number of positive, negative, and vanishing numbers in
    // the input
    double n_pos = 0;
    double n_neg = 0;
    double n_nil = 0;

    double temp;

    for (int i = 0; i < n; i++) {
        // Grab the number from stdin
        std::cin >> temp;

        // Count
        if (temp > 0) {
            n_pos++;
        } else if (temp < 0) {
            n_neg++;
        } else {
            n_nil++;
        }
    }

    // Make 'em fractions
    n_pos /= n;
    n_neg /= n;
    n_nil /= n;

    // Print the answers
    std::cout << n_pos << std::endl;
    std::cout << n_neg << std::endl;
    std::cout << n_nil << std::endl;

    return 0;
}
