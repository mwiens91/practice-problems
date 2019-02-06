#include <algorithm>
#include <iostream>

int main() {
    // Read input
    int n;
    int p;

    std::cin >> n >> p;

    // Turning from front
    int front_res = p / 2;
    int back_res = (n + (n + 1) % 2 - p) / 2;

    std::cout << std::min(front_res, back_res) << std::endl;

    return 0;
}
