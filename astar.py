#include <bits/stdc++.h>
using namespace std;

struct Node {
    double f, g;
    pair<int, int> pos;
    vector<pair<int, int>> path;

    bool operator>(const Node &other) const {
        return f > other.f;
    }
};

double heuristic(pair<int,int> a, pair<int,int> b) {
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

vector<pair<int,int>> a_star(vector<vector<int>> &grid, pair<int,int> start, pair<int,int> goal, double &final_cost) {
    int rows = grid.size(), cols = grid[0].size();
    vector<tuple<int,int,double>> directions = {
        {-1, 0, 1}, {1, 0, 1}, {0, -1, 1}, {0, 1, 1},
        {-1, -1, 1.5}, {-1, 1, 1.5}, {1, -1, 1.5}, {1, 1, 1.5}
    };

    priority_queue<Node, vector<Node>, greater<Node>> open_set;
    set<pair<int,int>> visited;

    Node start_node = {heuristic(start, goal), 0, start, {start}};
    open_set.push(start_node);

    while (!open_set.empty()) {
        Node current = open_set.top();
        open_set.pop();

        if (visited.count(current.pos)) continue;
        visited.insert(current.pos);

        if (current.pos == goal) {
            final_cost = current.g;
            return current.path;
        }

        for (auto &[dx, dy, cost] : directions) {
            int nx = current.pos.first + dx;
            int ny = current.pos.second + dy;

            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                if (!visited.count({nx, ny})) {
                    double new_g = current.g + cost;
                    double new_f = new_g + heuristic({nx, ny}, goal);

                    vector<pair<int,int>> new_path = current.path;
                    new_path.push_back({nx, ny});

                    open_set.push({new_f, new_g, {nx, ny}, new_path});
                }
            }
        }
    }

    final_cost = INFINITY;
    return {};
}

int main() {
    int n, m;
    cout << "Enter grid size (rows cols): ";
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m));
    cout << "Enter grid row by row (0 = river, 1 = land):\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    int sx, sy, gx, gy;
    cout << "Enter start position (row col): ";
    cin >> sx >> sy;
    cout << "Enter goal position (row col): ";
    cin >> gx >> gy;

    pair<int,int> start = {sx, sy}, goal = {gx, gy};
    double cost;
    vector<pair<int,int>> path = a_star(grid, start, goal, cost);

    if (!path.empty()) {
        cout << "Path found: ";
        for (auto &p : path) {
            cout << "(" << p.first << "," << p.second << ") ";
        }
        cout << "\nMinimum cost: " << cost << "\n";
    } else {
        cout << "No path found.\n";
    }

    return 0;
}

