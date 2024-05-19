/*
 * Program: prim.cpp
 * Date: 2024.05.19
 * Author: Nulla
 * Repository: Milton-Code
 * Description: Find the minimum tree by prim algorithm
 */

#include <iostream>
#include <vector>

using namespace std;

struct Vertex {
    char value;
    bool selected;
    int min_distance;
    int parent_index;

    Vertex(char x) : value(x), selected(false), min_distance(-1), parent_index(-1) {}
}

class Graph {
    vector<Vertex> vertices;
}
int main() {
    int
}
