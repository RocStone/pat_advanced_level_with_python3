#include <iostream>
#include <vector>
#include "climits"

using namespace std;

// start time: 2019-02-21 17-34-25 周四
// input: 4 5 0 3
//0 1 1 20
//1 3 2 30
//0 3 4 10
//0 2 2 20
//2 3 1 20
class Edge {
public:
    int u, v, dist, cost;

    Edge(int u, int v, int dist, int cost) {
        this->u = u;
        this->v = v;
        this->cost = cost;
        this->dist = dist;
    }
};

int N, M, S, D, total_dist = 0;
vector<vector<Edge>> edges;
vector<vector<Edge>> parents;
int dist_to[501];
bool visited[501];


void init() {
    cin >> N >> M >> S >> D;
    vector<vector<Edge>> edges2(N);
    edges = edges2;
    vector<vector<Edge>> parents2(N);
    parents = parents2;
    int u, v, dist, cost;
    for (int i = 0; i < M; ++i) {
        cin >> u >> v >> dist >> cost;
        Edge edge(u, v, dist, cost);
        edges[u].push_back(edge);
        Edge edge2(v, u, dist, cost);
        edges[v].push_back(edge2);
    }
    for (int &j : dist_to) {
        j = INT_MAX;
    }
    dist_to[S] = 0;
    for (bool &j : visited) {
        j = false;
    }
}

int find_nearest() {
    int tmp = INT_MAX, idx = -1;
    for (int i = 0; i < N; ++i) {
        if (not visited[i] and tmp > dist_to[i]) {
            tmp = dist_to[i];
            idx = i;
        }
    }
    return idx;
}

void update_nb(int idx) {
    for (Edge &edge : edges[idx]) {
        if (not visited[edge.v]) {
            if (dist_to[edge.v] > dist_to[idx] + edge.dist) {
                dist_to[edge.v] = dist_to[idx] + edge.dist;
                parents[edge.v].clear();
                parents[edge.v].push_back(edge);
            } else if (dist_to[edge.v] == dist_to[idx] + edge.dist) {
                parents[edge.v].push_back(edge);
            }
        }
    }
}

void dijkstra() {
    while (true) {
        int idx = find_nearest();
        if (idx == D) return;
        visited[idx] = true;
        update_nb(idx);
    }
}


int min_cost = INT_MAX;
vector<int> min_route;
vector<int> cur_route;

void dfs(int idx, int cur_cost) {
    if (idx == S) {
        if (cur_cost < min_cost) {
            min_route.assign(cur_route.begin(), cur_route.end());
            min_cost = cur_cost;
            return;
        }
    }
    for (Edge &edge : parents[idx]) {
        cur_route.push_back(edge.u);
        dfs(edge.u, cur_cost + edge.cost);
        cur_route.pop_back();
    }
}

void min_cost_way() {
    dfs(D, 0);
    int idx = D;
    while (idx != S) {
        total_dist += parents[idx][0].dist;
        idx = parents[idx][0].u;
    }
    for (int i = min_route.size() - 1; i >= 0; i--) {
        cout << min_route[i] << " ";
    }
    cout << D << " " << total_dist << " " << min_cost;
}

int main() {
    init();
    dijkstra();
    min_cost_way();
    return 0;
}

