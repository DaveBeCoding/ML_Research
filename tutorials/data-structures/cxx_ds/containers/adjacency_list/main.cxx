#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, vector<int> > adjList;

    // Add edges to the adjacency list
    adjList[0].push_back(1);
    adjList[0].push_back(2);
    adjList[1].push_back(2);
    adjList[2].push_back(0);
    adjList[2].push_back(3);
    adjList[3].push_back(3);

    // Print the adjacency list
    for (auto& pair : adjList) {
        cout << pair.first << ": ";
        for (int i : pair.second) {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}

