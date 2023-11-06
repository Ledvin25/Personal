#include <iostream>
#include <vector>
using namespace std;

class NodeInfo {
public:
    int id;
    char proteinType;

    NodeInfo(int nodeId, char type) : id(nodeId), proteinType(type) {}
};

class DirectedGraph {
private:
    int numNodes;
    vector<vector<pair<int, int>>> adjacencyList;

public:
    DirectedGraph(int n) : numNodes(n), adjacencyList(n) {}

    void addEdge(int from, int to, int weight) {
        adjacencyList[from].push_back({to, weight});
    }

    void DFS(int start, vector<bool>& visited, vector<int>& component) {
        visited[start] = true;
        component.push_back(start);

        for (const auto& neighbor : adjacencyList[start]) {
            if (!visited[neighbor.first]) {
                DFS(neighbor.first, visited, component);
            }
        }
    }

    vector<vector<int>> getConnectedComponents() {
        vector<bool> visited(numNodes, false);
        vector<vector<int>> connectedComponents;

        for (int i = 0; i < numNodes; ++i) {
            if (!visited[i]) {
                vector<int> component;
                DFS(i, visited, component);
                connectedComponents.push_back(component);
            }
        }

        return connectedComponents;
    }
};

int main() {
    const int totalNodes = 17; // 17 proteínas virales
    DirectedGraph graph(totalNodes);

    vector<NodeInfo> nodes;
    nodes.emplace_back(0, 'A');
    nodes.emplace_back(1, 'B');
    nodes.emplace_back(2, 'C');
    nodes.emplace_back(3, 'D');
    nodes.emplace_back(4, 'E');
    nodes.emplace_back(5, 'F');
    nodes.emplace_back(6, 'G');
    nodes.emplace_back(7, 'H');
    nodes.emplace_back(8, 'I');
    nodes.emplace_back(9, 'J');
    nodes.emplace_back(10, 'K');
    nodes.emplace_back(11, 'L');
    nodes.emplace_back(12, 'M');
    nodes.emplace_back(13, 'N');
    nodes.emplace_back(14, 'O');
    nodes.emplace_back(15, 'P');
    nodes.emplace_back(16, 'Q');

    // Establecer interacciones entre proteínas para formar 4 componentes
    graph.addEdge(0, 1, 1); // A-B
    graph.addEdge(1, 16, 1); // B-Q

    graph.addEdge(2, 3, 1); // C-D
    graph.addEdge(3, 4, 1); // D-E

    graph.addEdge(5, 6, 1); // F-G
    graph.addEdge(6, 7, 1); // G-H

    graph.addEdge(8, 9, 1); // I-J
    graph.addEdge(9, 10, 1); // J-K
    graph.addEdge(10, 11, 1); // K-L

    graph.addEdge(12, 13, 1); // M-N
    graph.addEdge(13, 14, 1); // N-O
    graph.addEdge(14, 15, 1); // O-P

    // Obtener componentes conexas
    auto connectedComponents = graph.getConnectedComponents();

    // Imprimir las componentes conexas
    for (const auto& component : connectedComponents) {
        cout << "Componente: ";
        for (int node : component) {
            cout << "Proteina: " << nodes[node].proteinType << " ";
        }
        cout << endl;
    }

    return 0;
}
